from django import forms
from .models import*

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

class CustomerNumberForm(forms.ModelForm):
    class Meta:
        model = CustomerPhone
        fields = "__all__"
    
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"

class OrderProductForm(forms.ModelForm):
    class Meta:
        model = Order_Product
        fields = "__all__"