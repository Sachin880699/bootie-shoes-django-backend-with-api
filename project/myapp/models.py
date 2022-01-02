from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()



class UserData(models.Model):
    name = models.CharField(max_length = 1000 , null = True , blank = True)
    address = models.CharField(max_length = 1000 , null = True , blank = True)
    mobile = models.CharField(max_length = 1000 , null = True , blank = True)

class SellingItems(models.Model):
    item_name = models.CharField(max_length =1000 , null = True , blank = True)
    image       = models.ImageField(upload_to = "selling_item_image" , null = True , blank = True)
    rating      = models.CharField(max_length =1000 , null = True , blank = True)
    price       = models.FloatField(null = True , blank = True)
    description = models.TextField(null = True , blank = True)

    def __str__(self):
        return self.item_name

class ContactUs(models.Model):
    name        = models.CharField(max_length = 1000 , null = True , blank = True)
    email       = models.CharField(max_length = 1000 , null = True , blank = True)
    phone_number = models.CharField(max_length = 1000 , null = True , blank = True)
    message     = models.TextField(null = True , blank = True)

    def __str__(self):
        return self.name

class SpecialDealOffer(models.Model):
    discount        = models.CharField(max_length = 2 , null = True , blank = True)
    discount_amount = models.CharField(max_length = 10000 , null = True , blank = True)
    sellingitem     = models.ForeignKey(SellingItems, on_delete=models.CASCADE , null = True , blank = True)

class LocalShop(models.Model):
    shop_owner      = models.ForeignKey(User , on_delete=models.CASCADE , null = True , blank = True)
    shop_name       = models.CharField(max_length = 1000 , null = True , blank = True)
    shop_address    = models.TextField(null = True , blank = True)
    phone_number    = models.CharField(max_length = 11 , null = True , blank = True)
    email           = models.CharField(max_length = 1000 , null = True , blank = True)
    rating          = models.CharField(max_length = 1000 , null = True , blank = True)
    description     = models.TextField(null = True , blank = True)

    def __str__(self):
        return self.shop_name
