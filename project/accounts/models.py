from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth import get_user_model
# from hotel.models import *

class UserRole(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    def create_user(self, username,  password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        # if not phone_number:
        #     raise ValueError('Users must have an phone_number')

        user = self.model(
            username=username,
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    objects        = UserManager()
    email          = models.CharField(max_length=254, null=True, blank=True)
    username       = models.CharField(max_length=254, null=True, blank=True , unique=True)
    first_name     = models.CharField(max_length=256, blank=True, null=True)
    last_name      = models.CharField(max_length=256, blank=True, null=True)
    profile_pic    = models.FileField(upload_to='profile_pic/', null=True, blank=True)
    role           = models.ManyToManyField(UserRole, related_name='user_role', null=True, blank=True)
    address        = models.CharField(max_length= 1000 , null= True , blank= True )
    divice_token   = models.CharField(max_length= 10000 , null= True , blank= True )
    divice_type    = models.CharField(max_length= 10000 , null= True , blank= True )
   


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []



    def __str__(self):
        # return str(self.phone_number) if self.phone_number else return str(self.username)
        if self.username:
            return str(self.username)
        


