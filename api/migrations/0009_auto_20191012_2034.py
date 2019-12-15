# Generated by Django 2.2.4 on 2019-10-12 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20191012_2005'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apartinfo',
            options={'verbose_name': 'Apart Bilgisi', 'verbose_name_plural': 'Apart Bilgileri'},
        ),
        migrations.AddField(
            model_name='apartinfo',
            name='bank_info',
            field=models.CharField(default='BANKA', max_length=256, verbose_name='Banka Bilgisi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apartinfo',
            name='iban',
            field=models.CharField(default='TR', max_length=50, verbose_name='IBAN'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='apartinfo',
            name='address_city',
            field=models.CharField(max_length=50, verbose_name='İl'),
        ),
        migrations.AlterField(
            model_name='apartinfo',
            name='address_district',
            field=models.CharField(max_length=50, verbose_name='İlçe'),
        ),
        migrations.AlterField(
            model_name='apartinfo',
            name='address_neighborhood',
            field=models.CharField(max_length=50, verbose_name='Mahalle'),
        ),
        migrations.AlterField(
            model_name='apartinfo',
            name='address_street',
            field=models.CharField(max_length=50, verbose_name='Cadde'),
        ),
        migrations.AlterField(
            model_name='apartinfo',
            name='short_title',
            field=models.CharField(max_length=255, verbose_name='Kısa İsim'),
        ),
        migrations.AlterField(
            model_name='apartinfo',
            name='title',
            field=models.CharField(max_length=255, verbose_name='İsim'),
        ),
        migrations.AlterField(
            model_name='room',
            name='landlord',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Landlord'),
        ),
    ]
