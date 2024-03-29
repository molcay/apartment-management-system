from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta


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
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Oda'
        verbose_name_plural = 'Odalar'

    def __str__(self):
        return "{} [{}]".format(self.human_readable_room_name, self.landlord.title)

    @property
    def human_readable_room_name(self):
        return "{} - {}/{}".format(self.building_number, self.home_number, self.room_number)


class Agreement(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    guarantor = models.ForeignKey(Guarantor, on_delete=models.CASCADE, null=True, blank=True)
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
        return '{}__{}__{}'.format(self.room.human_readable_room_name.replace(' ', '_').replace('/', '_'),
                                   self.tenant.name.replace(' ', '_'), self.id)


class AgreementFile(models.Model):
    agreement = models.ForeignKey(Agreement, on_delete=models.CASCADE)
    file = models.FileField('dosya')
    created_at = models.DateTimeField('Oluşturulma Tarihi', auto_now_add=True)

    class Meta:
        verbose_name = 'Anlaşma Dosyası'
        verbose_name_plural = 'Anlaşma Dosyaları'


class ApartInfo(models.Model):
    title = models.CharField('İsim', max_length=255)
    short_title = models.CharField('Kısa İsim', max_length=255)
    address_street = models.CharField('Cadde', max_length=50)
    address_neighborhood = models.CharField('Mahalle', max_length=50)
    address_district = models.CharField('İlçe', max_length=50)
    address_city = models.CharField('İl', max_length=50)
    bank_info = models.CharField('Banka Bilgisi', max_length=256)
    iban = models.CharField('IBAN', max_length=50)

    class Meta:
        verbose_name = "Apart Bilgisi"
        verbose_name_plural = "Apart Bilgileri"


class Issue(models.Model):
    summary = models.CharField('Arıza Tanımı', max_length=300)
    issue_type = models.CharField('Arıza Türü', max_length=50)
    created_at = models.DateTimeField('Oluşturulma Tarihi', auto_now_add=True)
    updated_at = models.DateTimeField('Güncellenme Tarihi', auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField('Arıza Durumu', max_length=50)
    reply = models.CharField('Arıza Geri Bildirimi', max_length=300)

    class Meta:
        verbose_name = 'Arıza'
        verbose_name_plural = 'Arızalar'

    def __str__(self):
        return self.summary


class Coupon(models.Model):
    coupon_code = models.CharField('Kupon Kodu', max_length=20)
    expire_in = models.IntegerField('İnternet Erişim Kodu Süresi')
    started_at = models.DateTimeField('Veriliş Tarihi', blank=True)
    given_to = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)    

    @property
    def expired_at(self):
        return self.started_at + timedelta(hours=self.expire_in)

    class Meta:
        verbose_name = 'İnternet Erişim Kodu'
        verbose_name_plural = 'İnternet Erişim Kodları'

    def __str__(self):
        return self.coupon_code