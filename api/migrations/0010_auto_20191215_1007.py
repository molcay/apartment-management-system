# Generated by Django 3.0 on 2019-12-15 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20191012_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='landlord',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Landlord'),
        ),
    ]
