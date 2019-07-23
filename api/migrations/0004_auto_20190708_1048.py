# Generated by Django 2.2.3 on 2019-07-08 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190708_1029'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agreement',
            options={'verbose_name': 'Anlaşma', 'verbose_name_plural': 'Anlaşmalar'},
        ),
        migrations.AlterModelOptions(
            name='guarantor',
            options={'verbose_name': 'Kefil', 'verbose_name_plural': 'Kefiller'},
        ),
        migrations.AlterModelOptions(
            name='landlord',
            options={'verbose_name': 'Mülk Sahibi', 'verbose_name_plural': 'Mülk Sahibleri'},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name': 'Oda', 'verbose_name_plural': 'Odalar'},
        ),
        migrations.AlterModelOptions(
            name='tenant',
            options={'verbose_name': 'Kiracı', 'verbose_name_plural': 'Kiracılar'},
        ),
        migrations.AddField(
            model_name='landlord',
            name='bank_info',
            field=models.CharField(default='qwe', max_length=256, verbose_name='Banka Bilgisi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='landlord',
            name='iban',
            field=models.CharField(default='TR', max_length=50, verbose_name='IBAN'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='agreement',
            name='dues',
            field=models.FloatField(verbose_name='Aidat Bedeli'),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='end_date',
            field=models.DateField(verbose_name='Kira Bitiş Tarihi'),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='lease_price',
            field=models.FloatField(verbose_name='Kira Bedeli'),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='start_date',
            field=models.DateField(verbose_name='Kira Başlangıç Tarihi'),
        ),
        migrations.AlterField(
            model_name='landlord',
            name='address',
            field=models.CharField(max_length=256, verbose_name='Adres'),
        ),
        migrations.AlterField(
            model_name='landlord',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Başlık/İsim'),
        ),
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.CharField(max_length=256, verbose_name='Adres'),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='İsim'),
        ),
        migrations.AlterField(
            model_name='person',
            name='gsm',
            field=models.CharField(max_length=11, verbose_name='Telefon Numarası'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Soyisim'),
        ),
        migrations.AlterField(
            model_name='person',
            name='tc',
            field=models.CharField(max_length=11, verbose_name='T.C Kimlik Numarası'),
        ),
        migrations.AlterField(
            model_name='person',
            name='work_address',
            field=models.CharField(max_length=256, verbose_name='İş Adresi'),
        ),
        migrations.AlterField(
            model_name='room',
            name='building_number',
            field=models.CharField(max_length=5, verbose_name='Bina Numarası'),
        ),
        migrations.AlterField(
            model_name='room',
            name='home_number',
            field=models.CharField(max_length=5, verbose_name='Ev Numarası'),
        ),
        migrations.AlterField(
            model_name='room',
            name='landlord',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Landlord'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_number',
            field=models.CharField(max_length=5, verbose_name='Oda Numarası'),
        ),
        migrations.AlterField(
            model_name='room',
            name='size',
            field=models.FloatField(verbose_name='Boyut'),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='email',
            field=models.CharField(max_length=50, verbose_name='E-Posta'),
        ),
    ]
