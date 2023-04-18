from modeltranslation.translator import register, TranslationOptions
from . import models

@register(models.News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description', 'keyword',)


@register(models.Web)
class WebTranslationOptions(TranslationOptions):
    fields = ('address', )


@register(models.Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'button',)


@register(models.Faq)
class FaqTranslationOptions(TranslationOptions):
    fields = ('question', 'answer',)


@register(models.LidersCategories)
class LidersCategoriesTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(models.Liders)
class LidersTranslationOptions(TranslationOptions):
    fields = ('model', 'country', 'postavshik', 'brend', 'description', 'pulbirligi',)
