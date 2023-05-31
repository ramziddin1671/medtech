from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from . import models


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title_uz', 'title_ru', 'subtitle_uz', 'subtitle_ru', 'description_uz',
                  'description_ru', 'date', 'views', 'image', 'keyword_uz', 'keyword_ru', )
        model = models.News


class WebSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'logo', 'address_uz', 'address_ru', 'email',
                  'phone', 'facebook', 'instagram', 'youtube', 'telegram',)
        model = models.Web


class BannerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title_uz', 'title_ru', 'description_uz',
                  'description_ru', 'image', 'button_uz', 'button_ru', 'button_phone',)
        model = models.Banner


class FaqSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('question_uz', 'question_ru', 'answer_uz', 'answer_ru',)
        model = models.Faq


class AboutSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title_uz', 'title_ru', 'description_uz', 'description_ru', 'video',)
        model = models.About


class PartnerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('logo', 'linkPartner',)
        model = models.Partners


class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'phon_number', 'message', 'organization',)
        model = models.Request


class RequestcallSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'phon_number',)
        model = models.RequestCall


class LidersCategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name_uz', 'name_ru',)
        model = models.LidersCategories


class LidersImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'image')
        model = models.LidersImage


class LidersSerializer(serializers.ModelSerializer):
    liders_images = LidersImageSerializer(many=True, read_only=True)
    category = LidersCategoriesSerializer(many=False, read_only=True)

    class Meta:
        fields = ('id', 'category', 'model_uz', 'model_ru', 'country_uz', 'country_ru', 'postavshik_uz', 'postavshik_ru',
                  'brend_uz', 'brend_ru', 'description_uz', 'description_ru', 'instagram', 'telegram', 'phone', 'email',
                  'image', 'price', 'pulbirligi_uz', 'pulbirligi_ru', 'views', 'touch',)
        model = models.Liders


class CategoryOborodvnyaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name_uz', 'name_ru',)
        model = models.CategoryOborodvnya


class EquipmentImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'image')
        model = models.EquipmentImage


class EquipmentSerializer(serializers.ModelSerializer):
    equipment_images = EquipmentImageSerializer(many=True, read_only=True)
    category = CategoryOborodvnyaSerializer(many=False, read_only=True)

    class Meta:
        fields = ('id', 'category', 'image', 'model_uz', 'model_ru', 'views', 'touch', 'country_uz', 'country_ru', 'supplier_uz', 'supplier_ru',
                  'brand_uz', 'brand_ru', 'description_uz', 'description_ru', 'instagram', 'telegram', 'phone', 'email',
                  'image', 'price', 'pulbirligi_uz', 'pulbirligi_ru', 'equipment_images',)
        model = models.Equipment


class CategoryReagentsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name_uz', 'name_ru',)
        model = models.CategoryReagents


class ReagentsSerializer(serializers.ModelSerializer):
    category = CategoryReagentsSerializer(many=False, read_only=True)

    class Meta:
        fields = ('id', 'category', 'model_uz', 'model_ru', 'title_uz', 'title_ru', 'releasedate',
                  'manufacturer_uz', 'manufacturer_ru', 'tests', 'supplier_uz', 'supplier_ru', 'phone', 'price',)
        model = models.Reagents


class CategoryConsumablesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name_uz', 'name_ru',)
        model = models.CategoryConsumables


class ConsumablesSerializer(serializers.ModelSerializer):
    category = CategoryConsumablesSerializer(many=False, read_only=True)

    class Meta:
        fields = ('id', 'category', 'model_uz', 'model_ru', 'title_uz', 'title_ru', 'unit',
                  'manufacturer_uz', 'manufacturer_ru', 'organization_uz', 'organization_ru', 'phone', 'price',)
        model = models.Consumables


class CategoryServiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name_uz', 'name_ru',)
        model = models.CategoryService


class PartsSerializer(serializers.ModelSerializer):
    category = CategoryServiceSerializer(many=False, read_only=True)

    class Meta:
        fields = ('id', 'category', 'title_uz', 'title_ru', 'unit',
                  'manufacturer_uz', 'manufacturer_ru', 'organization_uz', 'organization_ru', 'phone', 'price',)
        model = models.Parts


class RepairImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'image')
        model = models.RepairImage


class RepairSerializer(serializers.ModelSerializer):
    images = RepairImageSerializer(many=True, read_only=True)
    category = CategoryServiceSerializer(many=False, read_only=True)

    class Meta:
        fields = ('id', 'category', 'image', 'title_uz', 'title_ru', 'views', 'touch', 'organization_uz',  'organization_ru', 'description_uz',
                  'description_ru', 'instagram', 'telegram', 'phone', 'email', 'price', 'images',)
        model = models.Repair
