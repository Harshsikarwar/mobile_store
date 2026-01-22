from django.db import models

# Create your models here.
#username : admin, password : harsh@2005

class Customer(models.Model):
    customerId = models.CharField(max_length=10, primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    house = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    #derived attribute
    @property
    def full_name(self):
        return f"{self.fname} {self.lname}"
    
    def __str__(self):
        return f"{self.fname} {self.lname}"

#multiattribute table/model
class CustomerPhone(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.customer.customerId} : {self.phone}"

class Product(models.Model):
    avail_choices = [("IN","Available"),("OUT","Not Available")]

    prodId = models.CharField(max_length=10, primary_key=True)
    prodName = models.CharField(max_length=100)
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    availability = models.CharField(max_length=3, choices=avail_choices)

    def __str__(self):
        return self.prodName
    
class Order(models.Model):
    paymentChoice = [
        ('UPI','UPI Payment'),
        ('DBC','Debit Card Payment'),
        ('CBC','Credit Card Payment'),
        ('COD', 'Cash On Delivery')
    ]

    statusChoice = [("PLACED","Placed"),
                    ("SHIPPED","Shipped"),
                    ("DELIVERED","Delivered")
                    ]

    orderId = models.CharField(max_length=10, primary_key=True)

    #one to many relation between customer and order
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    status = models.CharField(max_length=20,choices=statusChoice, null=True)
    orderDate = models.DateField()
    paymentType = models.CharField(max_length=3, choices=paymentChoice)

    def __str__(self):
        return self.orderId
    
#many to many relation between products - order_product - order
class Order_Product(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('order','product')