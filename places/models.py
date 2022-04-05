from django.db import models


class Place(models.Model):
    placeId = models.CharField(
        max_length=200,
        verbose_name='Уникальный идентификатор места',
        blank=True
    )
    title = models.CharField(
        max_length=200,
        verbose_name='Название места',
        blank=True
    )
    project_title = models.CharField(
        max_length=200,
        verbose_name='Название проекта места',
        blank=True
    )
    description_short = models.TextField(
        verbose_name='Короткое описание',
        blank=True
    )
    description_long = models.TextField(
        verbose_name='Полное описание',
        blank=True
    )
    coordinates_lng = models.DecimalField(
        decimal_places=14,
        max_digits=16,
        blank=True,
        verbose_name='Долгота'
    )
    coordinates_lat = models.DecimalField(
        decimal_places=14,
        max_digits=16,
        blank=True,
        verbose_name='Широта'
    )

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.project_title


class Image(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    place = models.ForeignKey(
        Place,
        related_name='images',
        verbose_name='Место',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    position = models.IntegerField(verbose_name='Позиция', blank=True)
    photo = models.ImageField(verbose_name='Изображение')

    class Meta:
        ordering = ['position']
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return f'{self.id}. {self.name}'
