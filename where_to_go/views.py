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
                    "detailsUrl": {
                        "title": place.title,
                        "imgs": [
                            image.photo.url for image in place.images.all()
                        ],
                        "description_short": place.description_short,
                        "description_long": place.description_long,
                        "coordinates": {
                            "lat": place.coordinates_lat,
                            "lng": place.coordinates_lng,
                        },
                    },
                },
            },
        )
    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    return render(request, 'index.html', context=geojson)

