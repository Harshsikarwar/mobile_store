from django.contrib import admin
from .models import*
# Register your models here.

class CustomerDisplay(admin.ModelAdmin):
    list_display = ('customerId','email')
    search_fields = ('customerId', 'email')

class ProductDisplay(admin.ModelAdmin):
    list_display = ('prodId', 'prodName', 'availability')
    list_filter = ('availability',)

class OrderDisplay(admin.ModelAdmin):
    list_display = ('orderId', 'customer', 'paymentType','status')
    list_filter = ('paymentType',)

class OrderProductDisplay(admin.ModelAdmin):
    list_display = ('order','product','quantity','price')
    list_filter = ('order',)

admin.site.register(Customer,CustomerDisplay)
admin.site.register(CustomerPhone)
admin.site.register(Product,ProductDisplay)
admin.site.register(Order,OrderDisplay)
admin.site.register(Order_Product,OrderProductDisplay)