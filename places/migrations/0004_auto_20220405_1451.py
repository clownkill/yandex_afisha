# Generated by Django 3.2.12 on 2022-04-05 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20220404_1607'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['position']},
        ),
        migrations.AddField(
            model_name='image',
            name='position',
            field=models.IntegerField(blank=True, default=1, verbose_name='Позиция'),
            preserve_default=False,
        ),
    ]