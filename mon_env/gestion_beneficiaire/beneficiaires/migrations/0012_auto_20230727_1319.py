# Generated by Django 3.0 on 2023-07-27 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiaires', '0011_remove_beneficiaire_etat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informationoperation',
            name='date_ressencement',
            field=models.DateField(default='2023-01-01'),
        ),
    ]
