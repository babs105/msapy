# Generated by Django 4.2.7 on 2023-11-25 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carburant', '0004_alter_vehicule_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('quantite', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
            options={
                'verbose_name': 'Cuve',
                'verbose_name_plural': 'Cuves',
            },
        ),
        migrations.CreateModel(
            name='Ravitaillement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_heure_ravitaillement', models.DateTimeField()),
                ('quantite', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('cuve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carburant.cuve')),
                ('vehicule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carburant.vehicule')),
            ],
            options={
                'verbose_name': 'Ravitaillements',
                'verbose_name_plural': 'Ravitaillements',
            },
        ),
        migrations.AddField(
            model_name='cuve',
            name='vehicules',
            field=models.ManyToManyField(related_name='cuves', through='carburant.Ravitaillement', to='carburant.vehicule'),
        ),
    ]