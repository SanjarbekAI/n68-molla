from apps.pages.models import BannerModel
from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions


@register(BannerModel)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description','text',)