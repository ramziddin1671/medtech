from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='fill_data_index'),
    path('<str:model_slug>/', views.fill_data, name='fill_data'),
    path('<str:model_slug>/save/', views.save_data, name='save_data'),
]
