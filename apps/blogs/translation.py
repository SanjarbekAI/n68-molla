from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from apps.blogs.models import BlogModel, BlogTagModel, BlogCategoryModel, BlogAuthorModel


@register(BlogModel)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(BlogTagModel)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(BlogCategoryModel)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(BlogAuthorModel)
class NewsTranslationOptions(TranslationOptions):
    fields = ('full_name', 'bio',)
