from django import forms

class customer_form(forms.Form):
    customerId = forms.CharField(max_length=10)
    fname = forms.CharField(max_length=100)
    lname = forms.CharField(max_length=100)
    email = forms.EmailField()
    house = forms.CharField(max_length=100)
    street = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)

