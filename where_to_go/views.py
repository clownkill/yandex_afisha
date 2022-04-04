from django.shortcuts import render

from places.models import Place

def index(request):
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
                    "detailsUrl": place.detailsUrl
                }
            }
        )
    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    return render(request, 'index.html', context=geojson)

