from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from rest_framework import filters as rf_filters
from django_filters import rest_framework as filters

from . import paginations
from . import serializers
from . import models
# Create your views here.


class NewsList(generics.ListAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer
    pagination_class = paginations.PaginateBy16
    filter_backends = (rf_filters.SearchFilter,)
    search_fields = 'title_uz', 'title_ru', 'subtitle_uz', 'subtitle_ru', 'description_uz', 'description_ru', 'keyword'


class NewsDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer

    def get(self, request, pk):
        error_message = ("Obyekt topilmadi")
        try:
            news = models.News.objects.get(id=pk)
            news.views += 1
            news.save()
        except models.News.DoesNotExist:
            return Response({'error_message': error_message}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.NewsSerializer(
            news, context={"request": request})
        return Response(serializer.data)


class WebList(generics.ListAPIView):
    queryset = models.Web.objects.all()
    serializer_class = serializers.WebSerializer


class BannerList(generics.ListAPIView):
    queryset = models.Banner.objects.all()
    serializer_class = serializers.BannerSerializer


class FaqList(generics.ListAPIView):
    queryset = models.Faq.objects.all()
    serializer_class = serializers.FaqSerializer
    filter_backends = (rf_filters.SearchFilter,)
    search_fields = 'question_uz', 'question_ru', 'answer_uz', 'answer_ru'


class PartnerList(generics.ListAPIView):
    queryset = models.Partners.objects.all()
    serializer_class = serializers.PartnerSerializer


class RequestList(generics.ListCreateAPIView):
    queryset = models.Request.objects.all()
    serializer_class = serializers.RequestSerializer


class RequestDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = models.Request.objects.all()
    serializer_class = serializers.RequestSerializer


class RequestcallList(generics.ListCreateAPIView):
    queryset = models.RequestCall.objects.all()
    serializer_class = serializers.RequestcallSerializer


class RequestcallDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = models.RequestCall.objects.all()
    serializer_class = serializers.RequestcallSerializer


class LidersCategoriesList(generics.ListAPIView):
    queryset = models.LidersCategories.objects.all()
    serializer_class = serializers.LidersCategoriesSerializer


class LidersList(generics.ListAPIView):
    queryset = models.Liders.objects.all().order_by('-id')
    serializer_class = serializers.LidersSerializer


class LidersDetail(generics.RetrieveAPIView):
    queryset = models.Liders.objects.all()
    serializer_class = serializers.LidersSerializer

    def get(self, request, pk):
        error_message = ("Obyekt topilmadi")
        try:
            liders = models.Liders.objects.get(id=pk)
            liders.views += 1
            liders.save()
        except models.Liders.DoesNotExist:
            return Response({'error_message': error_message}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.LidersSerializer(
            liders, context={"request": request})
        return Response(serializer.data)


class LidersTouchAdd(APIView):
    def get(self, request, pk):
        liders = models.Liders.objects.filter(pk=pk).first()
        if liders:
            liders.touch += 1
            liders.save()
            return Response({'success': True})
        return Response({'success': False})


class CategoryOborodvnyaList(generics.ListAPIView):
    queryset = models.CategoryOborodvnya.objects.all()
    serializer_class = serializers.CategoryOborodvnyaSerializer


class EquipmentList(generics.ListAPIView):
    queryset = models.Equipment.objects.all().order_by('-id')
    serializer_class = serializers.EquipmentSerializer
    pagination_class = paginations.PaginateBy9
    filter_backends = (rf_filters.SearchFilter,
                       rf_filters.OrderingFilter,
                       filters.DjangoFilterBackend)
    search_fields = (
        'category__name_uz',
        'category__name_ru',
        'model_uz',
        'model_ru',
        'country_uz',
        'country_ru',
        'supplier_uz',
        'supplier_ru',
        'brand_uz',
        'brand_ru',
        'description_uz',
        'description_ru',
        'pulbirligi_uz',
        'pulbirligi_ru',
    )
    ordering_fields = (
        'model_uz',
        'model_ru',
        'country_uz',
        'country_ru',
        'supplier_uz',
        'supplier_ru',
        'brand_uz',
        'brand_ru',
    )
    filterset_fields = (
        'category__id',
    )


class EquipmentDetail(generics.RetrieveAPIView):
    queryset = models.Equipment.objects.all()
    serializer_class = serializers.LidersSerializer

    def get(self, request, pk):
        error_message = ("Obyekt topilmadi")
        try:
            Equipment = models.Equipment.objects.get(id=pk)
            Equipment.views += 1
            Equipment.save()
        except models.Equipment.DoesNotExist:
            return Response({'error_message': error_message}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.EquipmentSerializer(
            Equipment, context={"request": request})
        return Response(serializer.data)


class EquipmentTouchAdd(APIView):
    def get(self, request, pk):
        repair = models.Equipment.objects.filter(pk=pk).first()
        if repair:
            repair.touch += 1
            repair.save()
            return Response({'success': True})
        return Response({'success': False})


class CategoryReagentsList(generics.ListAPIView):
    queryset = models.CategoryReagents.objects.all()
    serializer_class = serializers.CategoryReagentsSerializer


class ReagentsList(generics.ListAPIView):
    queryset = models.Reagents.objects.all().order_by('-id')
    serializer_class = serializers.ReagentsSerializer
    pagination_class = paginations.PaginateBy25
    filter_backends = (rf_filters.SearchFilter,
                       rf_filters.OrderingFilter,
                       filters.DjangoFilterBackend)
    search_fields = (
        'category__name_uz',
        'category__name_ru',
        'model_uz',
        'model_ru',
        'title_uz',
        'title_ru',
        'releasedate',
        'manufacturer_uz',
        'manufacturer_ru',
        'tests',
        'price',
        'supplier_uz',
        'supplier_ru',
        'phone',
    )
    ordering_fields = (
        'category__name_uz',
        'category__name_ru',
        'model_uz',
        'model_ru',
        'title_uz',
        'title_ru',
        'releasedate',
        'manufacturer_uz',
        'manufacturer_ru',
        'tests',
        'price',
        'supplier_uz',
        'supplier_ru',
        'phone',
    )
    filterset_fields = (
        'category__id',
    )


class CategoryConsumablesList(generics.ListAPIView):
    queryset = models.CategoryConsumables.objects.all()
    serializer_class = serializers.CategoryConsumablesSerializer


class ConsumablesList(generics.ListAPIView):
    queryset = models.Consumables.objects.all().order_by('-id')
    serializer_class = serializers.ConsumablesSerializer
    pagination_class = paginations.PaginateBy25
    filter_backends = (rf_filters.SearchFilter,
                       rf_filters.OrderingFilter,
                       filters.DjangoFilterBackend)
    search_fields = (
        'category__name_uz',
        'category__name_ru',
        'model_uz',
        'model_ru',
        'title_uz',
        'title_ru',
        'unit',
        'manufacturer_uz',
        'manufacturer_ru',
        'organization_uz',
        'organization_ru',
        'price',
        'phone',
    )
    ordering_fields = (
        'category__name_uz',
        'category__name_ru',
        'model_uz',
        'model_ru',
        'title_uz',
        'title_ru',
        'unit',
        'manufacturer_uz',
        'manufacturer_ru',
        'organization_uz',
        'organization_ru',
        'price',
        'phone',
    )
    filterset_fields = (
        'category__id',
    )


class CategoryServiceList(generics.ListAPIView):
    queryset = models.CategoryService.objects.all()
    serializer_class = serializers.CategoryServiceSerializer


class PartsList(generics.ListAPIView):
    queryset = models.Parts.objects.all().order_by('-id')
    serializer_class = serializers.PartsSerializer
    pagination_class = paginations.PaginateBy25
    filter_backends = (rf_filters.SearchFilter,
                       rf_filters.OrderingFilter,
                       filters.DjangoFilterBackend)
    search_fields = (
        'category__name_uz',
        'category__name_ru',
        'title_uz',
        'title_ru',
        'unit',
        'manufacturer_uz',
        'manufacturer_ru',
        'organization_uz',
        'organization_ru',
        'price',
        'phone',
    )
    ordering_fields = (
        'category__name_uz',
        'category__name_ru',
        'title_uz',
        'title_ru',
        'unit',
        'manufacturer_uz',
        'manufacturer_ru',
        'organization_uz',
        'organization_ru',
        'price',
        'phone',
    )
    filterset_fields = (
        'category__id',
    )


class RepairList(generics.ListAPIView):
    queryset = models.Repair.objects.all().order_by('-id')
    serializer_class = serializers.RepairSerializer
    pagination_class = paginations.PaginateBy10
    filter_backends = (rf_filters.SearchFilter,
                       rf_filters.OrderingFilter,
                       filters.DjangoFilterBackend)
    search_fields = (
        'category__name_uz',
        'category__name_ru',
        'title_uz',
        'title_ru',
        'organization_uz',
        'organization_ru',
        'description_uz',
        'description_ru',
    )
    ordering_fields = (
        'category__name_uz',
        'category__name_ru',
        'title_uz',
        'title_ru',
        'organization_uz',
        'organization_ru',
    )
    filterset_fields = (
        'category__id',
    )


class RepairDetail(generics.RetrieveAPIView):
    queryset = models.Repair.objects.all()
    serializer_class = serializers.RepairSerializer

    def get(self, request, pk):
        error_message = ("Obyekt topilmadi")
        try:
            Repair = models.Repair.objects.get(id=pk)
            Repair.views += 1
            Repair.save()
        except models.Repair.DoesNotExist:
            return Response({'error_message': error_message}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.RepairSerializer(
            Repair, context={"request": request})
        return Response(serializer.data)


class RepairTouchAdd(APIView):
    def get(self, request, pk):
        repair = models.Repair.objects.filter(pk=pk).first()
        if repair:
            repair.touch += 1
            repair.save()
            return Response({'success': True})
        return Response({'success': False})
