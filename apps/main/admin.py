from django.contrib import admin
from .models import Catalog, Property, PropertyFiles, PropertyDetails, PropertyImages, CatalogVideo
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline


class CatalogA(admin.StackedInline):
    model = CatalogVideo
    extra = 1


@admin.register(Catalog)
class CatalogAdmin(TranslationAdmin):
    inlines = [CatalogA]

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class DetailAdmin(TranslationStackedInline):
    model = PropertyDetails
    extra = 1

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class FileAdmin(admin.StackedInline):
    model = PropertyFiles
    extra = 1


class ImageAdmin(admin.StackedInline):
    model = PropertyImages
    extra = 1


@admin.register(Property)
class PropertyAdmin(TranslationAdmin):
    inlines = [ImageAdmin, DetailAdmin, FileAdmin]

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
