from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
# Register your models here.


class PhotoInline(admin.StackedInline):
    model = EquipmentImage


@admin.register(Equipment)
class EquipmentAdmin(TranslationAdmin):

    list_display = ['category','views', 'touch', "image", 'model', 'country', 'supplier', 'brand', 'description', 'instagram',
                           'telegram', 'phone', 'email', 'price']
    inlines = [PhotoInline]


class PhotoRepair(admin.StackedInline):
    model = RepairImage


@admin.register(Repair)
class RepairAdmin(TranslationAdmin):
    list_display = ['category', 'image', 'title_uz', 'title_ru', 'views', 'touch', 'organization_uz',  'organization_ru', 'description_uz',
                  'description_ru', 'instagram', 'telegram', 'phone', 'email', 'price']

    inlines = [PhotoRepair]


class NewsAdmin(TranslationAdmin):
    model = News


class WebAdmin(TranslationAdmin):
    model = Web


class BannerAdmin(TranslationAdmin):
    model = Banner


class FaqAdmin(TranslationAdmin):
    model = Faq


class LidersCategoriesAdmin(TranslationAdmin):
    model = LidersCategories


class LidersAdmin(TranslationAdmin):
    model = Liders


class CategoryOborodvnyaAdmin(TranslationAdmin):
    model = CategoryOborodvnya


class CategoryReagentsAdmin(TranslationAdmin):
    model = CategoryReagents


class ReagentsAdmin(TranslationAdmin):
    model = Reagents


class CategoryConsumablesAdmin(TranslationAdmin):
    model = CategoryConsumables


class ConsumablesAdmin(TranslationAdmin):
    model = Consumables


class CategoryServiceAdmin(TranslationAdmin):
    model = CategoryService


class PartsAdmin(TranslationAdmin):
    model = Parts


# admin.site.register(Equipment, EquipmentGallerys)
admin.site.register(News, NewsAdmin)
admin.site.register(Web, WebAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(Partners)
admin.site.register(Request)
admin.site.register(RequestCall)
admin.site.register(LidersCategories, LidersCategoriesAdmin)
admin.site.register(Liders, LidersAdmin)
admin.site.register(CategoryOborodvnya, CategoryOborodvnyaAdmin)
admin.site.register(CategoryReagents, CategoryReagentsAdmin)
admin.site.register(Reagents, ReagentsAdmin)
admin.site.register(CategoryConsumables, CategoryConsumablesAdmin)
admin.site.register(Consumables, ConsumablesAdmin)
admin.site.register(CategoryService, CategoryServiceAdmin)
admin.site.register(Parts, PartsAdmin)
# admin.site.register(Repair, PepairGallerys)
