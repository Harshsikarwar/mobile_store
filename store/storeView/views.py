from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..models import*
from datetime import*
from ..forms import customer_form
from django.contrib import messages
# Create your views here.

#getters
def get_labels(filter = "1year"):
    label = []
    order = Order.objects.all()
    if filter == "1year":
        label = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
        return label
    elif filter == "2year":
        label = [str(int((datetime.today()).year)-1), (datetime.today()).year]
        return label
    elif filter == "3year":
        label = [str(int((datetime.today()).year)-2), str(int((datetime.today()).year)-1), (datetime.today()).year]
        return label
    elif filter == "month":
        label=[n for n in range(1,32)]
        return label
    else:
        print("invalid filter")

def get_data(filter = "1year"):
    orders = Order.objects.order_by("orderDate")
    order_product = Order_Product.objects.order_by("order")
    if filter == "month":
        orders = orders.filter(orderDate__month=str(date.today().month), orderDate__iso_year = str(date.today().year))
        data = [[n*0 for n in range(1,32)],0,0]
        for od in orders:
            for op in order_product:
                for currDay in range(1,32):
                    if (od.orderDate).day == currDay and od.orderId == str(op.order):
                        data[0][currDay-1] += op.price
                        data[1] += op.price
                        data[2] +=1
        return data
    if filter == "1year":
        orders = orders.filter(orderDate__iso_year = str(date.today().year))
        data = [[0,0,0,0,0,0,0,0,0,0,0,0],0,0]
        for od in orders:
            for op in order_product:
                if od.orderId == str(op.order):
                    data[0][int((od.orderDate).month)-1]+=(op.price)
                    data[1]+=(op.price)
                    data[2] +=1
        return data
    elif filter == "2year":
        orders = orders.filter(orderDate__iso_year = str(date.today().year)) | orders.filter(orderDate__iso_year = str(date.today().year-1))
        data = [[0,0],0,0]
        for od in orders:
            for op in order_product:
                if od.orderId == str(op.order) and (od.orderDate).year == int((datetime.today()).year)-1:
                    data[0][0]+=(op.price)
                    data[1]+=(op.price)
                    data[2] +=1
                if od.orderId == str(op.order) and (od.orderDate).year == (datetime.today()).year:
                    data[0][1]+=(op.price)
                    data[1]+=(op.price)
                    data[2] +=1
        return data
    elif filter == "3year":
        orders = orders.filter(orderDate__iso_year = str(date.today().year)) | orders.filter(orderDate__iso_year = str(date.today().year-1)) | orders.filter(orderDate__iso_year = str(date.today().year-2))
        data = [[0,0,0],0,0]
        for od in orders:
            for op in order_product:
                if od.orderId == str(op.order) and (od.orderDate).year == int((datetime.today()).year)-2:
                    data[0][0]+=(op.price)
                    data[1]+=(op.price)
                    data[2] +=1
                if od.orderId == str(op.order) and (od.orderDate).year == int((datetime.today()).year)-1:
                    data[0][1]+=(op.price)
                    data[1]+=(op.price)
                    data[2] +=1
                if od.orderId == str(op.order) and (od.orderDate).year == (datetime.today()).year:
                    data[0][2]+=(op.price)
                    data[1]+=(op.price)
                    data[2] +=1
        return data

def get_customer(count_all=True, all=False):
    customer = Customer.objects.all().order_by("customerId")
    if all != True:
        if count_all != True:
            return None
        total_customer = Customer.objects.count()
        return [total_customer,0]
    
    if count_all == True:
        total_customer = Customer.objects.count()
        return [total_customer,customer]
    return [0,customer]

def get_product(count_all=True, all=False):
    product = Product.objects.all().order_by("prodId")
    if all != True:
        if count_all != True:
            return None
        total_product = product.count()
        return [total_product,0]
    
    if count_all == True:
        total_product = product.count()
        return [total_product,product]
    return [0,product]

def get_order(count_all=True, all=False):
    order = Order.objects.all().order_by("orderId")
    if all != True:
        if count_all != True:
            return None
        total_order = order.count()
        return [total_order,0]
    
    if count_all == True:
        total_order = order.count()
        return [total_order,order]
    return [0,order]


#rendering views
def welcome(request):
    return render(request,"store/welcome.html")  

def home(request):
    label = get_labels()
    data = get_data()
    total_customer = get_customer()[0]
    total_product = get_product()[0]
    if request.method == 'POST':
        filter = request.POST.get("filter")
        label = get_labels(filter)
        data = get_data(filter)
        print(data)
        return render(request, "store/home.html",{"label":label,
                                                  "data":data[0],
                                                  "sortby":f"{filter} - sales report",
                                                  "net_sales_price":data[1],
                                                  "total_order":data[2],
                                                  "total_customer":total_customer,
                                                  "total_product":total_product
                                                  })
    return render(request, "store/home.html",{"label":label,
                                              "data":data[0],
                                              "sortby":"year - sales report",
                                              "net_sales_price":data[1],
                                              "total_order":data[2],
                                              "total_customer":total_customer,
                                              "total_product":total_product
                                              })

def customer(request):
    customers = get_customer(all=True,count_all=True)
    customer_phone = CustomerPhone.objects.all().order_by("customer")
    if request.method == "POST":
        if "search_query" in request.POST:
            search_by = request.POST.get("search_by")
            search_value = request.POST.get("search_value")
            if search_by == "customer_id" and search_value != "":
                if not customers[1].filter(customerId = search_value).exists():
                    messages.error(request,"customer id not found")
                    return redirect("/store/customer/")
                customers[1]=customers[1].filter(customerId = search_value)
                customer_phone=customer_phone.filter(customer__in=customers[1]) 
            elif search_by == "fname" and search_value != "":
                if not customers[1].filter(fname = search_value).exists():
                    messages.error(request,"fname not found")
                    return redirect("/store/customer/")
                customers[1]=customers[1].filter(fname=search_value)
                customer_phone=customer_phone.filter(customer__in=customers[1]) 
            elif search_by == "lname" and search_value != "":
                if not customers[1].filter(lname = search_value).exists():
                    messages.error(request,"lname not found")
                    return redirect("/store/customer/")
                customers[1]=customers[1].filter(lname = search_value)
                customer_phone=customer_phone.filter(customer__in=customers[1]) 
            elif search_by == "email" and search_value != "":
                if not customers[1].filter(email = search_value).exists():
                    messages.error(request,"email not found")
                    return redirect("/store/customer/")
                customers[1]=customers[1].filter(email = search_value) 
                customer_phone=customer_phone.filter(customer__in=customers[1]) 
            elif search_by == "city" and search_value != "":
                if not customers[1].filter(ciyt = search_value).exists():
                    messages.error(request,"city not found")
                    return redirect("/store/customer/")
                customers[1]=customers[1].filter(city = search_value)
                customer_phone=customer_phone.filter(customer__in=customers[1]) 
            elif search_by == "state" and search_value != "":
                if not customers[1].filter(state = search_value).exists():
                    messages.error(request,"state not found")
                    return redirect("/store/customer/")
                customers[1]=customers[1].filter(state = search_value)  
                customer_phone=customer_phone.filter(customer__in=customers[1])
            else:
                print("view : invalid : customer")      
        if "reset" in request.POST:
            customers = get_customer(all=True)
        
        if "name_sort" in request.POST:
            sortby = request.POST.get("sort_by")
            if "ascending" == sortby:
                customers[1]=customers[1].order_by("fname")
            else:
                customers[1]=customers[1].order_by("-fname")
        
        if "id_sort" in request.POST:
            sortby = request.POST.get("sort_by")
            if "ascending" == sortby:
                customers[1]=customers[1].order_by("customerId")
            else:
                customers[1]=customers[1].order_by("-customerId")
    return render(request, "store/customer.html",
                  {"customers":customers[1],
                   "total_customer":customers[0],
                   "customer_phone":customer_phone})

def product(request):
    products = get_product(all=True,count_all=False)
    if request.method == "POST":
        if "search_query" in request.POST:
            search_by = request.POST.get("search_by")
            search_value = request.POST.get("search_value")
            if search_by == "prod_id" and search_value != "":
                if not products[1].filter(prodId = search_value).exists():
                    messages.error(request,"product id not found")
                    return redirect("/store/product/")
                products[1]=products[1].filter(prodId = search_value)
            elif search_by == "prod_name" and search_value != "":
                if not products[1].filter(prodName = search_value).exists():
                    messages.error(request,"product name not found")
                    return redirect("/store/product/")
                products[1]=products[1].filter(prodName=search_value) 
            elif search_by == "availability" and search_value != "":
                if not products[1].filter(availability = search_value).exists():
                    messages.error(request,"availability not found")
                    return redirect("/store/product/")
                products[1]=products[1].filter(availability = search_value)     
            else:
                print("view : invalid : product") 
        if "reset" in request.POST:
            products = get_product(all=True, count_all=False)
        
        if "name_sort" in request.POST:
            sortby = request.POST.get("sort_by")
            if "ascending" == sortby:
                products[1]=products[1].order_by("prodName")
            else:
                products[1]=products[1].order_by("-prodName")
        
        if "id_sort" in request.POST:
            sortby = request.POST.get("sort_by")
            if "ascending" == sortby:
                products[1]=products[1].order_by("prodId")
            else:
                products[1]=products[1].order_by("-prodId")
    return render(request, "store/product.html",
                  {"products":products[1],
                   "total_product":products[0]})

def order(request):
    orders = get_order(all=True,count_all=False)
    order_product = Order_Product.objects.all().order_by("order")
    if request.method == "POST":
        if "search_query" in request.POST:
            search_by = request.POST.get("search_by")
            search_value = request.POST.get("search_value")

            if search_by == "order_id" and search_value != "":
                if not orders[1].filter(orderId = search_value).exists():
                    messages.error(request,"order id not found")
                    return redirect("/store/order/")
                orders[1]=orders[1].filter(orderId = search_value)
                order_product=order_product.filter(order__in=orders[1]) 

            elif search_by == "status" and search_value != "":
                if not orders[1].filter(status = search_value).exists():
                    messages.error(request,"status id not found")
                    return redirect("/store/order/")
                orders[1]=orders[1].filter(status = search_value)
                order_product=order_product.filter(order__in=orders[1]) 

            elif search_by == "payment_type" and search_value != "":
                if not orders[1].filter(paymentType = search_value).exists():
                    messages.error(request,"payment type not found")
                    return redirect("/store/order/")
                orders[1]=orders[1].filter(paymentType = search_value)
                order_product=order_product.filter(order__in=orders[1]) 

            else:
                print("view : invalid : product") 

        if "reset" in request.POST:
            orders = get_order(all=True)
        
        if "name_sort" in request.POST:
            sortby = request.POST.get("sort_by")
            if "ascending" == sortby:
                orders[1]=orders[1].order_by("prodName")
            else:
                orders[1]=orders[1].order_by("-prodName")
        
        if "id_sort" in request.POST:
            sortby = request.POST.get("sort_by")
            if "ascending" == sortby:
                orders[1]=orders[1].order_by("prodId")
            else:
                orders[1]=orders[1].order_by("-prodId")
    return render(request, "store/order.html",
                  {"orders":orders[1],
                   "total_order":orders[0],
                   "order_product":order_product})
