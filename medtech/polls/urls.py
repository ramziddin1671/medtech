from django.urls import path
from . import views


urlpatterns = [
    path("news/", views.NewsList.as_view()),
    path("news/<int:pk>/", views.NewsDetail.as_view()),
    path("webcontact/", views.WebList.as_view()),
    path("banner/", views.BannerList.as_view()),
    path("faq/", views.FaqList.as_view()),
    path("about/", views.About.as_view()),
    path("partners/", views.PartnerList.as_view()),
    path("request/", views.RequestList.as_view()),
    path("request/<int:pk>/", views.RequestDetail.as_view()),
    path("requestcall/", views.RequestcallList.as_view()),
    path("requestcall/<int:pk>/", views.RequestcallDetail.as_view()),
    path("LidersCategories/", views.LidersCategoriesList.as_view()),
    path("LidersList/", views.LidersList.as_view()),
    path("LidersDetail/<int:pk>/", views.LidersDetail.as_view()),
    path("LidersTouchAdd/<int:pk>/", views.LidersTouchAdd.as_view()),
    path("CategoryOborodvnya/", views.CategoryOborodvnyaList.as_view()),
    path("EquipmentList/", views.EquipmentList.as_view()),
    path("EquipmentDetail/<int:pk>/", views.EquipmentDetail.as_view()),
    path("EquipmentTouchAdd/<int:pk>/", views.EquipmentTouchAdd.as_view()),
    path("CategoryReagents/", views.CategoryReagentsList.as_view()),
    path("ReagentList/", views.ReagentsList.as_view()),
    path("CategoryConsumables/", views.CategoryConsumablesList.as_view()),
    path("Consumableslist/", views.ConsumablesList.as_view()),
    path("CategoryService/", views.CategoryServiceList.as_view()),
    path("PartsList/", views.PartsList.as_view()),
    path("RepairList/", views.RepairList.as_view()),
    path("RepairDetail/<int:pk>/", views.RepairDetail.as_view()),
    path("RepairTouchAdd/<int:pk>/", views.RepairTouchAdd.as_view()),
]
