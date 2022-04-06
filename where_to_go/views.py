from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, reverse

from places.models import Place


def get_geojson():
    places = Place.objects.all()
    features = []

    for place in places:
        features.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.coordinates_lng, place.coordinates_lat]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse(place_json, args=[place.pk]),
                },
            },
        )

    geojson = {
      "type": "FeatureCollection",
      "features": features
    }

    return geojson


def index(request):
    return render(request, 'index.html', {'geojson': get_geojson()})


def place_json(request, place_id):
    place = get_object_or_404(Place, pk=place_id)

    page_response_data = {
        "title": place.title,
        "imgs": [image.photo.url for image in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.coordinates_lat,
            "lng": place.coordinates_lng,
        },
    }

    return JsonResponse(
        page_response_data,
        safe=False,
        json_dumps_params={'ensure_ascii': False}
    )
