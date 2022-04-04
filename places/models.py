from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название места')
    description_short = models.TextField(verbose_name='Короткое описание', blank=True)
    description_long = models.TextField(verbose_name='Полное описание', blank=True)
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

    def __str__(self):
        return self.title


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
    photo = models.ImageField(verbose_name='Изображение', )

    def __str__(self):
        return f'{self.id}. {self.name}'
