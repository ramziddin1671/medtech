from django.urls import path
from . import views


urlpatterns = [
    path("news/", views.NewsList.as_view()),
    path("news/<int:pk>/", views.NewsDetail.as_view()),
    path("webcontact/", views.WebList.as_view()),
    path("banner/", views.BannerList.as_view()),
    path("faq/", views.FaqList.as_view()),
    path("partners/", views.PartnerList.as_view()),
    path("request/", views.RequestList.as_view()),
    path("request/<int:pk>/", views.RequestDetail.as_view()),
    path("requestcall/", views.RequestcallList.as_view()),
    path("requestcall/<int:pk>/", views.RequestcallDetail.as_view()),
    path("LidersCategories/", views.LidersCategoriesList.as_view()),
    path("LidersList/", views.LidersList.as_view()),
    path("LidersDetail/<int:pk>/", views.LidersDetail.as_view()),
]
