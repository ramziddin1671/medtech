import datetime
from rest_framework import serializers
from . import models
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _
import json


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title_uz', 'title_ru', 'subtitle_uz', 'subtitle_ru', 'description_uz', 'description_ru', 'date', 'views', 'image', 'keyword_uz', 'keyword_ru', )
        model = models.News


class WebSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'logo', 'address_uz', 'address_ru', 'email', 'phone', 'facebook', 'instagram', 'youtube', 'telegram',)
        model = models.Web


class BannerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title_uz', 'title_ru', 'description_uz', 'description_ru', 'image', 'button_uz', 'button_ru', 'button_phone',)
        model = models.Banner


class FaqSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('question_uz', 'question_ru', 'answer_uz', 'answer_ru',)
        model = models.Faq


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
    # subdivisions = serializers.SerializerMethodField()

    class Meta:
        fields = ('id', 'name_uz', 'name_ru',)
        model = models.LidersCategories

    # def get_subdivisions(self, instance):
    #     subdivisions = models.Liders.objects.filter(category=instance).order_by('category')
    #     return LidersSerializer(subdivisions, many=True, context={"request": self.context.get("request")}).data


class LidersSerializer(serializers.ModelSerializer):
    # liderscategories = serializers.StringRelatedField()

    class Meta:
        fields = ('id', 'category', 'model_uz', 'model_ru', 'country_uz', 'country_ru', 'postavshik_uz', 'postavshik_ru',
                  'brend_uz', 'brend_ru', 'description_uz', 'description_ru','instagram','telegram','phone','email',
                  'image', 'price', 'pulbirligi_uz', 'pulbirligi_ru',)
        model = models.Liders
        read_only_fields = ['liderscategories', ]
        order_by = ['position', ]
