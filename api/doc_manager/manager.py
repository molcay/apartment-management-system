import os

from django.conf import settings
from docxtpl import DocxTemplate, RichText

from api.models import Agreement
from project.utils.TurkishUtils import TurkishUtils


class DocManager:
    def __init__(self, template_file):
        self._config = settings.DOC_MANAGER
        self._template_path = self._config.get('TEMPLATES').get('DIR')
        self._generated_path = self._config.get('GENERATED').get('DIR')
        self._create_path()

        self.filename = self._get_template_file_name(template_file)
        self.doc = DocxTemplate(self.filename)

        print(self._config)

    def _create_path(self):
        if not os.path.isdir(self._generated_path):
            print("Not found. Creating...")
            os.mkdir(self._generated_path)

    def _get_template_file_name(self, filename):
        return os.path.join(self._template_path, filename)

    def _get_generated_file_name(self, agreement):
        filename = "{}.docx".format(agreement.filename)
        return os.path.join(self._generated_path, filename)

    @staticmethod
    def get_rich_text(txt: str, **kwargs) -> 'RichText':
        return RichText(txt, font='Arial', **kwargs)

    @staticmethod
    def get_bold_text(txt: str) -> 'RichText':
        return DocManager.get_rich_text(txt, bold=True)

    @staticmethod
    def to_template_context(agreement: Agreement) -> dict:
        birim_kira_bedeli_str = "{}. ({})".format(
            TurkishUtils.currency_to_human_readable(agreement.lease_price),
            'OKUNUŞ BURAYA GELECEK'
        )
        birim_aidat_bedeli_str = "{}. ({})".format(
            TurkishUtils.currency_to_human_readable(agreement.dues),
            'OKUNUŞ BURAYA GELECEK'
        )
        yillik_kira_bedeli_str = "{}. ({})".format(
            TurkishUtils.currency_to_human_readable(agreement.lease_price * 10),
            'OKUNUŞ BURAYA GELECEK'
        )  # TODO: change * 10 with how many months last the lease.
        yillik_aidat_bedeli_str = "{}. ({})".format(
            TurkishUtils.currency_to_human_readable(agreement.dues * 10),
            'OKUNUŞ BURAYA GELECEK'
        )  # TODO: change * 10 with how many months last the lease.

        data = {
            'dis_kapi_no': DocManager.get_bold_text(agreement.room.building_number),
            'daire_no': DocManager.get_bold_text(agreement.room.home_number),
            'oda_no': DocManager.get_bold_text(agreement.room.room_number),
            'metre_kare': DocManager.get_bold_text('({} m²)'.format(str(agreement.room.size).replace('.', ','))),
            'kiraya_veren': DocManager.get_bold_text(agreement.room.landlord.title),
            'kiraya_veren_adres': DocManager.get_rich_text(agreement.room.landlord.address),
            'kiraci_ad': DocManager.get_bold_text(agreement.tenant.name.upper()),
            'kiraci_adres': DocManager.get_rich_text(agreement.tenant.address),
            'kiraci_tc': DocManager.get_rich_text(agreement.tenant.tc),
            'kiraci_gsm': DocManager.get_rich_text(agreement.tenant.gsm),
            'kiraci_email': DocManager.get_rich_text(agreement.tenant.email),
            'birim_kira_bedeli': DocManager.get_bold_text(birim_kira_bedeli_str),
            'birim_aidat_bedeli': DocManager.get_bold_text(birim_aidat_bedeli_str),
            'yillik_kira_bedeli': DocManager.get_bold_text(yillik_kira_bedeli_str),
            'yillik_aidat_bedeli': DocManager.get_bold_text(yillik_aidat_bedeli_str),
        }

        if agreement.guarantor is not None:
            data.update({
                'kefil_ad': DocManager.get_bold_text(agreement.guarantor.name.upper()),
                'kefil_adres': DocManager.get_rich_text(agreement.guarantor.address),
                'kefil_tc': DocManager.get_rich_text(agreement.guarantor.tc),
                'kefil_gsm': DocManager.get_rich_text(agreement.guarantor.gsm),
            })

        return data

    def create(self, agreement: Agreement) -> str:
        self.doc.render(DocManager.to_template_context(agreement))

        filename_to_save = self._get_generated_file_name(agreement)
        print(filename_to_save)
        self.doc.save(filename_to_save)

        return filename_to_save
