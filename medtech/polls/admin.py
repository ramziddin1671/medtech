from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
# Register your models here.


class PhotoInline(admin.StackedInline):
    model = EquipmentImage


@admin.register(Equipment)
class EquipmentAdmin(TranslationAdmin):

    list_display = ['category','views', 'touch', "image", 'model', 'country', 'supplier', 'brand', 'description', 'subtitle', 'instagram',
                           'telegram', 'phone', 'email', 'price']
    inlines = [PhotoInline]


class PhotoRepair(admin.StackedInline):
    model = RepairImage


@admin.register(Repair)
class RepairAdmin(TranslationAdmin):
    list_display = ['category', 'image', 'title_uz', 'title_ru', 'views', 'touch', 'organization_uz',  'organization_ru', 'description_uz',
                  'description_ru', 'instagram', 'telegram', 'phone', 'email', 'price', 'pulbirligi']

    inlines = [PhotoRepair]


class PhotoLider(admin.StackedInline):
    model = LidersImage


@admin.register(Liders)
class LidersAdmin(TranslationAdmin):
    list_display = ['category', 'model_uz', 'model_ru', 'country_uz', 'country_ru', 'postavshik_uz', 'postavshik_ru', 'brend_uz',  'brend_ru', 'description_uz',
                  'description_ru', 'instagram', 'telegram', 'phone', 'email', 'price', 'image', 'pulbirligi_uz', 'pulbirligi_ru', 'views', 'touch']

    inlines = [PhotoLider]


class NewsAdmin(TranslationAdmin):
    model = News


class AboutAdmin(TranslationAdmin):
    model = About


class WebAdmin(TranslationAdmin):
    model = Web


class BannerAdmin(TranslationAdmin):
    model = Banner


class FaqAdmin(TranslationAdmin):
    model = Faq


class LidersCategoriesAdmin(TranslationAdmin):
    model = LidersCategories





class CategoryOborodvnyaAdmin(TranslationAdmin):
    model = CategoryOborodvnya


class CategoryReagentsAdmin(TranslationAdmin):
    model = CategoryReagents

@admin.register(Reagents)
class RepairAdmin(TranslationAdmin):
    list_display = ['category', 'model_uz', 'model_ru', 'title_uz', 'title_ru', 'releasedate',
                  'manufacturer_uz', 'manufacturer_ru', 'tests', 'supplier_uz', 'supplier_ru', 'phone', 'price']


class CategoryConsumablesAdmin(TranslationAdmin):
    model = CategoryConsumables


@admin.register(Consumables)
class ConsumablesAdmin(TranslationAdmin):
    list_display = ['category', 'model_uz', 'model_ru', 'title_uz', 'title_ru', 'unit',
                  'manufacturer_uz', 'manufacturer_ru', 'organization_uz', 'organization_ru', 'phone', 'price']


class CategoryServiceAdmin(TranslationAdmin):
    model = CategoryService


@admin.register(Parts)
class ConsumablesAdmin(TranslationAdmin):
    list_display = ['category', 'title_uz', 'title_ru', 'unit',
                  'manufacturer_uz', 'manufacturer_ru', 'organization_uz', 'organization_ru', 'phone', 'price']


# admin.site.register(Equipment, EquipmentGallerys)
admin.site.register(About, AboutAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Web, WebAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(Partners)
admin.site.register(Request)
admin.site.register(RequestCall)
admin.site.register(LidersCategories, LidersCategoriesAdmin)
admin.site.register(CategoryOborodvnya, CategoryOborodvnyaAdmin)
admin.site.register(CategoryReagents, CategoryReagentsAdmin)
admin.site.register(CategoryConsumables, CategoryConsumablesAdmin)
admin.site.register(CategoryService, CategoryServiceAdmin)
# admin.site.register(Repair, PepairGallerys)
