from modeltranslation.translator import register, TranslationOptions
from . import models

@register(models.News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description', 'keyword',)


@register(models.Web)
class WebTranslationOptions(TranslationOptions):
    fields = ('address', )


@register(models.About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


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


@register(models.CategoryOborodvnya)
class CategoryOborodvnyaTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(models.Equipment)
class EquipmentTranslationOptions(TranslationOptions):
    fields = ('model', 'country', 'supplier', 'brand', 'description', 'subtitle', 'pulbirligi',)


@register(models.CategoryReagents)
class CategoryReagentsTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(models.Reagents)
class ReagentsTranslationOptions(TranslationOptions):
    fields = ('model', 'title', 'manufacturer', 'supplier',)


@register(models.CategoryConsumables)
class CategoryConsumablesTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(models.Consumables)
class ConsumablesTranslationOptions(TranslationOptions):
    fields = ('model', 'title', 'manufacturer', 'organization',)


@register(models.CategoryService)
class CategoryServiceTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(models.Parts)
class PartsTranslationOptions(TranslationOptions):
    fields = ('title', 'manufacturer', 'organization',)


@register(models.Repair)
class RepairTranslationOptions(TranslationOptions):
    fields = ('title', 'organization', 'description', 'pulbirligi',)
