from django.db import models


class Person(models.Model):
    first_name = models.CharField('İsim', max_length=50)
    last_name = models.CharField('Soyisim', max_length=50)
    address = models.CharField('Adres', max_length=256)
    work_address = models.CharField('İş Adresi', max_length=256)
    tc = models.CharField('T.C Kimlik Numarası', max_length=11)
    gsm = models.CharField('Telefon Numarası', max_length=11)

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return "{} [{}]".format(self.name, self.tc)


class Tenant(Person):
    email = models.CharField('E-Posta', max_length=50)

    class Meta:
        verbose_name = 'Kiracı'
        verbose_name_plural = 'Kiracılar'


class Guarantor(Person):
    class Meta:
        verbose_name = 'Kefil'
        verbose_name_plural = 'Kefiller'


class Landlord(models.Model):
    title = models.CharField('Başlık/İsim', max_length=50)
    address = models.CharField('Adres', max_length=256)
    bank_info = models.CharField('Banka Bilgisi', max_length=256)
    iban = models.CharField('IBAN', max_length=50)

    class Meta:
        verbose_name = 'Mülk Sahibi'
        verbose_name_plural = 'Mülk Sahibleri'

    def __str__(self):
        return self.title


class Room(models.Model):
    building_number = models.CharField('Bina Numarası', max_length=5)  # 110, 112
    home_number = models.CharField('Ev Numarası', max_length=5)  # 1,2,3, 13Ç
    room_number = models.CharField('Oda Numarası', max_length=5)  # A, B, C
    size = models.FloatField('Boyut')  # 12.80 m2 room
    landlord = models.ForeignKey(Landlord, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Oda'
        verbose_name_plural = 'Odalar'

    def __str__(self):
        return "{} [{}]".format(self.human_readable_room_name, self.landlord.title)

    @property
    def human_readable_room_name(self):
        return "{} - {}/{}".format(self.building_number, self.home_number, self.room_number)


class Agreement(models.Model):
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING)
    tenant = models.ForeignKey(Tenant, on_delete=models.DO_NOTHING)
    guarantor = models.ForeignKey(Guarantor, on_delete=models.DO_NOTHING, null=True, blank=True)
    start_date = models.DateField('Kira Başlangıç Tarihi')
    end_date = models.DateField('Kira Bitiş Tarihi')
    lease_price = models.FloatField('Kira Bedeli')  # Kira Bedeli
    dues = models.FloatField('Aidat Bedeli')  # Aidat

    class Meta:
        verbose_name = 'Anlaşma'
        verbose_name_plural = 'Anlaşmalar'

    def __str__(self):
        return '"{}" numaralı oda "{}" tarafından tutuldu.'.format(self.room, self.tenant.name)

    @property
    def filename(self):
        return '{}__{}__{}'.format(self.room.human_readable_room_name.replace(' ', '_').replace('/', '_'), self.tenant.name.replace(' ', '_'), self.id)


class AgreementFile(models.Model):
    agreement = models.ForeignKey(Agreement, on_delete=models.DO_NOTHING)
    file = models.FileField('dosya')
    created_at = models.DateTimeField('Oluşturulma Tarihi', auto_now_add=True)

    class Meta:
        verbose_name = 'Anlaşma Dosyası'
        verbose_name_plural = 'Anlaşma Dosyaları'
