# Generated by Django 3.0 on 2019-12-15 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0010_auto_20191215_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='landlord',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Landlord'),
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=300, verbose_name='Arıza Tanımı')),
                ('issue_type', models.CharField(max_length=50, verbose_name='Arıza Türü')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
                ('status', models.CharField(max_length=50, verbose_name='Arıza Durumu')),
                ('reply', models.CharField(max_length=300, verbose_name='Arıza Geri Bildirimi')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Arıza',
                'verbose_name_plural': 'Arızalar',
            },
        ),
    ]
