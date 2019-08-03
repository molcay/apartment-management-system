# Generated by Django 2.2.3 on 2019-07-10 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190708_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='landlord',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Landlord'),
        ),
        migrations.CreateModel(
            name='AgreementFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='', verbose_name='dosya')),
                ('agreement', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Agreement')),
            ],
        ),
    ]