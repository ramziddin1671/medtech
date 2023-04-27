from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from . import paginations
from . import serializers
from . import models
# Create your views here.

class NewsList(generics.ListAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer
    pagination_class = paginations.PaginateBy16


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
        serializer = serializers.NewsSerializer(news, context={"request": request})
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
        serializer = serializers.LidersSerializer(liders, context={"request": request})
        return Response(serializer.data)


class CategoryOborodvnyaList(generics.ListAPIView):
    queryset = models.CategoryOborodvnya.objects.all()
    serializer_class = serializers.CategoryOborodvnyaSerializer


class EquipmentList(generics.ListAPIView):
    queryset = models.Equipment.objects.all().order_by('-id')
    serializer_class = serializers.EquipmentSerializer
    pagination_class = paginations.PaginateBy9


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
        serializer = serializers.EquipmentSerializer(Equipment, context={"request": request})
        return Response(serializer.data)


class CategoryReagentsList(generics.ListAPIView):
    queryset = models.CategoryReagents.objects.all()
    serializer_class = serializers.CategoryReagentsSerializer


class ReagentsList(generics.ListAPIView):
    queryset = models.Reagents.objects.all().order_by('-id')
    serializer_class = serializers.ReagentsSerializer
    pagination_class = paginations.PaginateBy25


class CategoryConsumablesList(generics.ListAPIView):
    queryset = models.CategoryConsumables.objects.all()
    serializer_class = serializers.CategoryConsumablesSerializer


class ConsumablesList(generics.ListAPIView):
    queryset = models.Consumables.objects.all().order_by('-id')
    serializer_class = serializers.ConsumablesSerializer
    pagination_class = paginations.PaginateBy25


class CategoryServiceList(generics.ListAPIView):
    queryset = models.CategoryService.objects.all()
    serializer_class = serializers.CategoryServiceSerializer


class PartsList(generics.ListAPIView):
    queryset = models.Parts.objects.all().order_by('-id')
    serializer_class = serializers.PartsSerializer
    pagination_class = paginations.PaginateBy25


class RepairList(generics.ListAPIView):
    queryset = models.Repair.objects.all().order_by('-id')
    serializer_class = serializers.RepairSerializer
    pagination_class = paginations.PaginateBy10


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
        serializer = serializers.RepairSerializer(Repair, context={"request": request})
        return Response(serializer.data)
