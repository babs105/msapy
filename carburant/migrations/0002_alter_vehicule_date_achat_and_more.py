# Generated by Django 4.2.7 on 2023-11-25 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carburant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicule',
            name='date_achat',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehicule',
            name='date_mise_en_service',
            field=models.DateField(blank=True, null=True),
        ),
    ]
