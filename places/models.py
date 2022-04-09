from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название места',
        blank=True
    )
    description_short = models.TextField(
        verbose_name='Короткое описание',
        blank=True
    )
    description_long = HTMLField(
        verbose_name='Полное описание',
        blank=True
    )
    coordinates_lng = models.DecimalField(
        decimal_places=14,
        max_digits=16,
        verbose_name='Долгота'
    )
    coordinates_lat = models.DecimalField(
        decimal_places=14,
        max_digits=16,
        verbose_name='Широта'
    )

    class Meta:
        ordering = ['title']
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title


class Image(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    place = models.ForeignKey(
        Place,
        related_name='images',
        verbose_name='Место',
        on_delete=models.CASCADE
    )
    photo = models.ImageField(verbose_name='Изображение')
    position = models.PositiveIntegerField(
        verbose_name='Позиция',
        default=0,
        blank=False,
        null=False
    )

    class Meta:
        ordering = ['position']
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.name
