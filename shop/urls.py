from . import views
from django.urls import path

urlpatterns = [
    path('', views.shop_home, name="shop_home"),
    path('item/<int:pk>/', views.shop_item_details, name="shop_item_details"),
]
