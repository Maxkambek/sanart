from modeltranslation.translator import register, TranslationOptions
from .models import Catalog, Property, PropertyDetails


@register(Catalog)
class CatalogTrans(TranslationOptions):
    fields = ('name',)


@register(Property)
class PropertyTrans(TranslationOptions):
    fields = ('name', 'address', 'description')


@register(PropertyDetails)
class DetailTrans(TranslationOptions):
    fields = ('key', 'value')
