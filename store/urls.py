from django.urls import path
from .storeView import views,managmentView

urlpatterns = [
    path("", views.welcome, name="welcome" ),
    path("home/", views.home, name="home"),
    path("customer/", views.customer, name="customer"),
    path("product/", views.product, name="product"),
    path("order/", views.order, name="order"),
    path("create_customer/", managmentView.createCustomer, name="createCustomer"),
    path("update_customer/<str:customerId>/", managmentView.updateCustomer, name="updateCustomer"),
    path("delete_customer/<str:customerId>/", managmentView.deleteCustomer, name="deleteCustomer")
]