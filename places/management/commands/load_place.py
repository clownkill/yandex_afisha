from pathlib import Path
from urllib.parse import urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Image, Place


class Command(BaseCommand):
    help = 'Введите ссылку на json-файл интересного места'

    def add_arguments(self, parser):
        parser.add_argument('load_place', nargs='+', type=str)

    def handle(self, *args, **options):
        for url in options.get('load_place'):
            response = requests.get(url)
            response.raise_for_status()
            place_details = response.json()

            place, _ = Place.objects.get_or_create(
                title=place_details['title'],
                defaults={
                    'description_short': place_details['description_short'],
                    'description_long': place_details['description_long'],
                    'coordinates_lng': place_details['coordinates']['lng'],
                    'coordinates_lat': place_details['coordinates']['lat']
                }
            )

            for image_number, image_url in enumerate(place_details['imgs'], 1):
                response = requests.get(image_url)
                response.raise_for_status()
                content = ContentFile(response.content)
                name = Path(urlparse(image_url).path).name
                new_image = Image(place=place, position=image_number)
                new_image.photo.save(name, content, save=True)