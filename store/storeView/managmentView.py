from django.shortcuts import render, redirect, get_object_or_404
from ..models import*
from datetime import*
from ..forms import*
from django.contrib import messages

#Customer
def updateCustomer(request, customerId):
    customer = get_object_or_404(Customer, customerId=customerId)
    customerNumber = get_object_or_404(CustomerPhone, customer__in=customerId)

    if request.method == "POST":
        form = CustomerForm(request.POST,instance=customer)
        numberForm = CustomerNumberForm(request.POST, instance=customerNumber)
        #passing form data to customer form
        #instance use to tell form we want to only update
        if form.is_valid():
            form.save()
            numberForm.save()
            return redirect("/store/customer/")
    else:
        form = CustomerForm(instance=customer)
        numberForm = CustomerNumberForm(instance=customerNumber)
    return render(request, "store/manage.html", {"form":form, "numberForm":numberForm, "title":"Update Customer"})

def createCustomer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        numberForm = CustomerNumberForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/store/customer/")
    else:
        form = CustomerForm
        numberForm = CustomerNumberForm
        
    return render(request, "store/manage.html", {"form":form, "numberForm":numberForm, "title":"Create Customer"})

def deleteCustomer(request, customerId):
    customer = get_object_or_404(Customer, customerId=customerId)
    customer.delete()
    return redirect("/store/customer/")

#Contact

def addContact(request):
    if request.method == 'POST':
        form = CustomerNumberForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/store/customer/")
    else:
        form = CustomerNumberForm

    return render(request, "store/manage.html", {"form":form, "title":"Add Contact"})

def updateContact(request, contact):
    customerNumber = get_object_or_404(CustomerPhone, phone=contact)

    if request.method == 'POST':
        form = CustomerNumberForm(request.POST, instance=customerNumber)

        if form.is_valid():
            form.save()
            return redirect("/store/customer/")
    else:
        form = CustomerNumberForm(instance=customerNumber)
    
    return render(request, "store/manage.html", {"form":form})

def deleteContact(request, contact):
    customerNumber = get_object_or_404(CustomerPhone, phone=contact)
    customerNumber.delete()
    return redirect("/store/customer/")