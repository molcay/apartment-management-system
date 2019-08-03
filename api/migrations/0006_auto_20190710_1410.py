# Generated by Django 2.2.3 on 2019-07-10 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190710_1240'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agreementfile',
            options={'verbose_name': 'Anlaşma Dosyası', 'verbose_name_plural': 'Anlaşma Dosyaları'},
        ),
        migrations.AddField(
            model_name='agreementfile',
            name='created_at',
            field=models.DateTimeField(auto_created=True, auto_now=True, verbose_name='Oluşturulma Tarihi'),
        ),
        migrations.AlterField(
            model_name='room',
            name='landlord',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Landlord'),
        ),
    ]