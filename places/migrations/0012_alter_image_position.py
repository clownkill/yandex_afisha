# Generated by Django 4.0.3 on 2022-04-09 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0011_alter_image_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='position',
            field=models.PositiveIntegerField(blank=True, verbose_name='Позиция'),
        ),
    ]
