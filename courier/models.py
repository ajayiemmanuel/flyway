from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.db import models


# Create your models here.
class Customer (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    address = models.CharField (max_length = 200,  null = True)
    phone_number = models.CharField (max_length = 200, null = True)
    country = models.CharField (max_length = 200, null = True)
    city = models.CharField (max_length = 200, null = True)


    def __str__(self):
        return self.name



class Product (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    order = models.CharField (max_length = 200, null = True)
    expected_arrival = models.CharField (max_length = 200,  null = True)
    usps = models.CharField (max_length = 200, null = True)
    destination = models.CharField (max_length = 200, null = True)
    delivery = models.CharField (max_length = 200, null = True)
    package_name = models.CharField (max_length = 200, null = True)
    order_date = models.CharField (max_length = 200, null = True)
    delivery_date = models.CharField (max_length = 200, null = True)
    reciever_name = models.CharField (max_length = 200, null = True)    
    status = models.CharField (max_length = 200, null = True)
    address = models.CharField (max_length = 200, null = True)
    phone_number = models.CharField (max_length = 200, null = True)
    postal_code = models.CharField (max_length = 200, null = True)
    profile_pic = models.ImageField (default = "ship.jpg", null = True, blank = True)
    origin = models.CharField (max_length = 200, null = True)
    shipping_amount = models.CharField (max_length = 200, null = True)
    method_of_payment = models.CharField (max_length = 200, null = True, default="Mastercard")
    description = models.CharField (max_length = 200, null = True)
    weight = models.CharField (max_length = 200, null = True, default="12.5Kg")
    service_type = models.CharField (max_length = 200, null = True, default="International")
    tracking_id = models.CharField (max_length = 200, null = True, default="")
    movement = models.CharField (max_length = 200, null = True, default="Hold")


    def __str__(self):
        return self.name        



class Tracking (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    first_step = models.CharField (max_length = 200, null = True, default="Processing...")
    second_step = models.CharField (max_length = 200,  null = True, default="Processing...")
    third_step = models.CharField (max_length = 200, null = True, default="Processing...")
    fourth_step = models.CharField (max_length = 200, null = True, default="Processing...")
    fifth_step = models.CharField (max_length = 200, null = True, default="Processing...")
    sixth_step = models.CharField (max_length = 200, null = True, default="Processing...")


    def __str__(self):
        return self.name    

