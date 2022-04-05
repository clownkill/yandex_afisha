from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

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
                    "placeId": place.placeId,
                    "detailsUrl": place.detailsUrl,
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


def page(request, id):
    place = get_object_or_404(Place, pk=id)
    return HttpResponse(place.project_title)
