from django.db import models




class UserData(models.Model):
    name = models.CharField(max_length = 1000 , null = True , blank = True)
    address = models.CharField(max_length = 1000 , null = True , blank = True)
    mobile = models.CharField(max_length = 1000 , null = True , blank = True)

class SellingItems(models.Model):
    item_name = models.CharField(max_length =1000 , null = True , blank = True)
    image       = models.ImageField(upload_to = "selling_item_image" , null = True , blank = True)
    rating      = models.CharField(max_length =1000 , null = True , blank = True)
    price       = models.FloatField(null = True , blank = True)

    def __str__(self):
        return self.item_name

class ContactUs(models.Model):
    name        = models.CharField(max_length = 1000 , null = True , blank = True)
    email       = models.CharField(max_length = 1000 , null = True , blank = True)
    phone_number = models.CharField(max_length = 1000 , null = True , blank = True)
    message     = models.TextField(null = True , blank = True)

    def __str__(self):
        return self.name