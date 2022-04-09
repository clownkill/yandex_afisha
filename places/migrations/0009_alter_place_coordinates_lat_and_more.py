# Generated by Django 4.0.3 on 2022-04-09 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_alter_place_options_remove_place_placeid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='coordinates_lat',
            field=models.DecimalField(decimal_places=14, max_digits=16, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='place',
            name='coordinates_lng',
            field=models.DecimalField(decimal_places=14, max_digits=16, verbose_name='Долгота'),
        ),
    ]
