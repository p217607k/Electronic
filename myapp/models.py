from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.db import models
import datetime

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length= 200)
    def __str__(self):
        return self.name
class Brand(models.Model):
    name = models.CharField(max_length= 200)
    def __str__(self):
        return self.name
class Color(models.Model):
    name = models.CharField(max_length= 200)
    code = models.CharField(max_length= 200)
    def __str__(self):
        return self.name
class Filter_price(models.Model):
    filter_price=(
        ('200 T0 500','200 T0 500'),
        ('500 T0 1000','500 T0 1000'),
        ('1000 T0 2000','10 T0 2000'),
        ('2000 T0 3000','2000 T0 3000'),
        ('3000 T0 4000','3000 T0 4000'),
        ('5000 T0 10000','5000 T0 10000'),
        )
    price = models.CharField(choices=filter_price,max_length =100)
class Product(models.Model):
    status = (('Public','Public'),('Draft','Draft'))
    condition = (('New','New'),('Old','Old'))
    stack =(('In Stack','In Stack'),('Out Of Stack','Out Of Stack'))
    unique_id = models.CharField(unique = True,max_length = 202,null =True,blank =True)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image =models.ImageField(upload_to ='Electronic/mega')
    category =models.ForeignKey(Categories,on_delete=models.CASCADE)
    color =models.ForeignKey(Color,on_delete=models.CASCADE)
    brand =models.ForeignKey(Brand,on_delete=models.CASCADE)
    filter_price =models.ForeignKey(Filter_price,on_delete=models.CASCADE)
    datetime = models.DateTimeField(default= timezone.now)
    condition = models.CharField(choices=condition,max_length=200)
    stock=models.CharField(choices=stack,max_length=200)
    statu=models.CharField( choices=status ,max_length=250)
    information = RichTextField(blank=True,null=True)
    dec = RichTextField(blank=True,null=True)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.unique_id is None and self.datetime and self.id:
            self.unique_id = self.datetime.strftime('75%Y%m%d23') + str(self.id)
        return super().save(*args, **kwargs)

class  Images(models.Model):
    image =models.ImageField(upload_to ='Electronic/mega')
    product = models.ForeignKey(Product,on_delete =models.CASCADE)
class tag(models.Model):
    name = models.CharField(max_length = 200)
    product = models.ForeignKey(Product,on_delete =models.CASCADE)
    def __str__(self):
        return self.name
class contect_us(models.Model):
    name = models.CharField(max_length =100)
    email = models.EmailField(max_length =100)
    subject = models.TextField(max_length =100)
    message=models.TextField(max_length =1000)
    def __str__(self):
        return self.name

class Order(models.Model):
    # image = models.ImageField(upload_to = 'Ecommerce/Order')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    email = models.EmailField(max_length =100)
    address = models.CharField(max_length =100)
    country = models.CharField(max_length =100)
    state = models.CharField(max_length =100)
    city = models.CharField(max_length =100,null =True)
    pincode = models.IntegerField(null =True)
    payment_id = models.CharField(max_length =300,null =True,blank=True)
    paid = models.BooleanField(null =True,blank=True)
    phone = models.CharField(max_length =100)
    datetime = models.DateField(default=datetime.date.today())
    # additional_info = models.TextField()
    
    def __str__(self):
        return self.user.username

class OrderItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null = True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE,null = True)
    image = models.ImageField(upload_to = 'Ecommerce/Order')
    product = models.CharField(max_length=100)
    price = models.IntegerField(max_length =100,default='')
    quantity = models.IntegerField(max_length =100)
    total = models.CharField(max_length =100,default='')
    
    # def __str__(self):
    #     return self.Order.user.username
    