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
    
