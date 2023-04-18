from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
# Register your models here.


class PhotoInline(admin.StackedInline):
    model = EquipmentImage


class EquipmentGallerys(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['category','views', 'touch', "image", 'model', 'country', 'supplier', 'brand', 'description', 'instagram',
                           'telegram', 'phone', 'email', 'price']})
    ]
    inlines = [PhotoInline]


class PhotoRepair(admin.StackedInline):
    model = RepairImage


class PepairGallerys(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ["category", 'title', 'image', 'views', 'touch', 'organization', 'description', 'instagram', 'telegram',
                           'phone', 'email', 'price']})
    ]
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


admin.site.register(Equipment, EquipmentGallerys)
admin.site.register(News, NewsAdmin)
admin.site.register(Web, WebAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(Partners)
admin.site.register(Request)
admin.site.register(RequestCall)
admin.site.register(LidersCategories, LidersCategoriesAdmin)
admin.site.register(Liders, LidersAdmin)
admin.site.register(CategoryOborodvnya)
admin.site.register(CategoryReagents)
admin.site.register(Reagents)
admin.site.register(CategoryConsumables)
admin.site.register(Consumables)
admin.site.register(CategoryService)
admin.site.register(Parts)
admin.site.register(Repair, PepairGallerys)
