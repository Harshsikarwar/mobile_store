from django.shortcuts import render, redirect, get_object_or_404
from ..models import*
from datetime import*
from ..forms import*
from django.contrib import messages

#Customer
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
    return render(request, "store/manage.html", {"form":form, "title":"Update Customer"})

def createCustomer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/store/customer/")
    else:
        form = CustomerForm
        
    return render(request, "store/manage.html", {"form":form, "title":"Create Customer"})

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
    
    return render(request, "store/manage.html", {"form":form,  "title":"Update Contact"})

def deleteContact(request, contact):
    customerNumber = get_object_or_404(CustomerPhone, phone=contact)
    customerNumber.delete()
    return redirect("/store/customer/")

#Product

def addProduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/store/product/")
    else:
        form = ProductForm
    
    return render(request, "store/manage.html", {"form":form, "title":"Add Product"})

def updateProduct(request, prodId):
    product = get_object_or_404(Product, prodId=prodId)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("/store/product/")
    else:
        form = ProductForm(instance=product)
    
    return render(request, "store/manage.html/", {"form":form, "title":"Update Product"})

def deleteProduct(request, prodId):
    product = get_object_or_404(Product, prodId=prodId)
    product.delete()
    return redirect("/store/product/")

#Order
def createOrder(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/store/order/")
    else:
        form = OrderForm
    return render(request, "store/manage.html/", {"form":form})

def updateOrder(request, orderId):
    order = get_object_or_404(Order, orderId=orderId)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("/store/order/")
    else:
        form = OrderForm(instance=order)
    return render(request, "store/manage.html/", {"form":form})

def deleteOrder(request, orderId):
    order = get_object_or_404(Order, orderId=orderId)
    order.delete()
    return redirect("/store/order/")

#Order-Product

def addOrderProduct(request):
    if request.method == 'POST':
        form = OrderProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/store/order/")
    else:
        form = OrderProductForm
    return render(request, "store/manage.html/", {"form":form})

def updateOrderProduct(request, orderId, prodId):
    orderProduct = get_object_or_404(Order_Product, order=orderId, product=prodId)
    if request.method == 'POST':
        form = OrderProductForm(request.POST, instance=orderProduct)
        if form.is_valid():
            form.save()
            return redirect("/store/order/")
    else:
        form = OrderProductForm(instance=orderProduct)
    return render(request, "store/manage.html/", {"form":form})

def deleteOrderProduct(request, orderId, prodId):
    orderProduct = get_object_or_404(Order_Product, order=orderId, product=prodId)
    orderProduct.delete()
    return redirect("/store/order/")