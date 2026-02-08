from django.urls import path
from .storeView import views

urlpatterns = [
    path("", views.welcome, name="welcome" ),
    path("home/", views.home, name="home"),
    path("customer/", views.customer, name="customer"),
    path("product/", views.product, name="product"),
    path("order/", views.order, name="order")
]