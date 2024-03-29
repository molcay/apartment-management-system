# Generated by Django 3.0 on 2019-12-22 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0012_merge_20191222_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='landlord',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Landlord'),
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_code', models.CharField(max_length=20, verbose_name='Kupon Kodu')),
                ('start_date', models.DateTimeField(auto_now_add=True, verbose_name='Veriliş Tarihi')),
                ('expired_date', models.DateTimeField(auto_now=True, verbose_name='Son Kullanma Tarihi')),
                ('given_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'İnternet Erişim Kodları',
                'verbose_name_plural': 'İnternet Erişim Kodları',
            },
        ),
    ]
