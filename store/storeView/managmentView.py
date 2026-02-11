from django.shortcuts import render, redirect, get_object_or_404
from ..models import*
from datetime import*
from ..forms import CustomerForm
from django.contrib import messages

def updateCustomer(request, customerId):
    customer = get_object_or_404(Customer, customerId=customerId)
    if request.method == "POST":
        form = CustomerForm(request.POST,instance=customer)
        #passing form data to customer form
        #instance use to tell form we want to only update
        if form.is_valid():
            form.save()
            return redirect("/store/customer/")
    else:
        form = CustomerForm(instance=customer)
    return render(request, "store/manageCustomer.html", {"form":form})

def createCustomer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/store/customer/")
    else:
        form = CustomerForm
        
    return render(request, "store/createCustomer.html", {"form":form})

def deleteCustomer(request, customerId):
    customer = Customer.objects.filter(customerId=customerId)
    customer.delete()
    return redirect("/store/customer/")