from modeltranslation.translator import register, TranslationOptions
from .models import News, Contact


@register(News)
class NewsTrans(TranslationOptions):
    fields = ('title', 'content')


@register(Contact)
class ContactTrans(TranslationOptions):
    fields = ('address', 'time')
