# Generated by Django 4.2.7 on 2023-12-08 19:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carburant', '0008_rename_ravitaillement_ravitaillementcuve_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ravitaillementcuve',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]