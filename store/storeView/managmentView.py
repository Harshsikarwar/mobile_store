from django.shortcuts import render, redirect, get_object_or_404
from ..models import*
from datetime import*
from ..forms import*
from django.contrib import messages
from django.contrib.auth.decorators import login_required 

#Customer
@login_required(login_url="/account/logout/")
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

@login_required(login_url="/account/logout/")
def createCustomer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/store/customer/")
    else:
        form = CustomerForm
        
    return render(request, "store/manage.html", {"form":form, "title":"Create Customer"})

@login_required(login_url="/account/logout/")
def deleteCustomer(request, customerId):
    customer = get_object_or_404(Customer, customerId=customerId)
    customer.delete()
    return redirect("/store/customer/")

#Contact

@login_required(login_url="/account/logout/")
def addContact(request):
    if request.method == 'POST':
        form = CustomerNumberForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/store/customer/")
    else:
        form = CustomerNumberForm

    return render(request, "store/manage.html", {"form":form, "title":"Add Contact"})

@login_required(login_url="/account/logout/")
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

@login_required(login_url="/account/logout/")
def deleteContact(request, contact):
    customerNumber = get_object_or_404(CustomerPhone, phone=contact)
    customerNumber.delete()
    return redirect("/store/customer/")

#Product

@login_required(login_url="/account/logout/")
def addProduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/store/product/")
    else:
        form = ProductForm
    
    return render(request, "store/manage.html", {"form":form, "title":"Add Product"})

@login_required(login_url="/account/logout/")
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

@login_required(login_url="/account/logout/")
def deleteProduct(request, prodId):
    product = get_object_or_404(Product, prodId=prodId)
    product.delete()
    return redirect("/store/product/")

#Order

@login_required(login_url="/account/logout/")
def createOrder(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/store/order/")
    else:
        form = OrderForm
    return render(request, "store/manage.html/", {"form":form, "title":"Create Order"})

@login_required(login_url="/account/logout/")
def updateOrder(request, orderId):
    order = get_object_or_404(Order, orderId=orderId)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("/store/order/")
    else:
        form = OrderForm(instance=order)
    return render(request, "store/manage.html/", {"form":form, "title":"Update Order"})

@login_required(login_url="/account/logout/")
def deleteOrder(request, orderId):
    order = get_object_or_404(Order, orderId=orderId)
    order.delete()
    return redirect("/store/order/")

#Order-Product

@login_required(login_url="/account/logout/")
def addOrderProduct(request):
    if request.method == 'POST':
        form = OrderProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/store/order/")
    else:
        form = OrderProductForm
    return render(request, "store/manage.html/", {"form":form, "title":"Add Order-Product"})

@login_required(login_url="/account/logout/")
def updateOrderProduct(request, orderId, prodId):
    orderProduct = get_object_or_404(Order_Product, order=orderId, product=prodId)
    if request.method == 'POST':
        form = OrderProductForm(request.POST, instance=orderProduct)
        if form.is_valid():
            quantity = form.cleaned_data["quantity"]
            product = Product.objects.get(prodId=prodId)
            product_quantity = product.quantity
            if product_quantity < quantity:
                messages.info(request,"Insufficent Qunatity")
                return redirect(f"/store/update_orderproduct/{orderId}/{prodId}/")
            form.save()
            return redirect("/store/order/")
    else:
        form = OrderProductForm(instance=orderProduct)
    return render(request, "store/manage.html/", {"form":form, "title":"Update Order-Product"})

@login_required(login_url="/account/logout/")
def deleteOrderProduct(request, orderId, prodId):
    orderProduct = get_object_or_404(Order_Product, order=orderId, product=prodId)
    orderProduct.delete()
    return redirect("/store/order/")