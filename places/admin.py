from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    fields = ['place', 'photo', 'get_preview', 'position']
    extra = 0
    readonly_fields = ['get_preview']

    def get_preview(self, place):
        return format_html('<img src="{}" width="auto", height="200px"/>', place.photo.url)

@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ['place', ]
