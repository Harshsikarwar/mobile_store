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
    path("delete_customer/<str:customerId>/", managmentView.deleteCustomer, name="deleteCustomer"),
    
    path("add_contact/", managmentView.addContact, name="addContact"),
    path("update_contact/<str:contact>/", managmentView.updateContact, name="updateContact"),
    path("delete_contact/<str:contact>/", managmentView.deleteContact, name="deleteContact"),
    
    path("add_product/", managmentView.addProduct, name="addProduct"),
    path("update_product/<str:prodId>/", managmentView.updateProduct, name="updateProduct"),
    path("delete_product/<str:prodId>/", managmentView.deleteProduct, name="deleteProduct"),

    path("create_order/", managmentView.createOrder, name="addProduct"),
    path("update_order/<str:orderId>/", managmentView.updateOrder, name="updateOrder"),
    path("delete_order/<str:orderId>/", managmentView.deleteOrder, name="deleteOrder"),

    path("add_orderproduct/", managmentView.addOrderProduct, name="addProduct"),
    path("update_orderproduct/<str:orderId>/<str:prodId>/", managmentView.updateOrderProduct, name="updateOrderProduct"),
    path("delete_orderproduct/<str:orderId>/<str:prodId>/", managmentView.deleteOrderProduct, name="deleteOrderProduct"),
]