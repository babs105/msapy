# Generated by Django 4.2.7 on 2023-12-10 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connexion', '0002_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='Default.jpeg', null=True, upload_to='profile/'),
        ),
    ]