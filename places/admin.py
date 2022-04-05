from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    fields = ['place', 'photo', 'get_preview', 'position']
    readonly_fields = ["get_preview"]

    def get_preview(self, place):
        return mark_safe(f'<img src="{place.photo.url}" width="auto" height="200px" />')

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Image)
