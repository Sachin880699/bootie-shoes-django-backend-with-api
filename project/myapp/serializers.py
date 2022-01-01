from.models import *
from rest_framework import serializers
from django.contrib import auth
from accounts.models import *


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model  = UserData
        fields = '__all__'


class SellingItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellingItems
        fields = '__all__'

class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fiels = '__all__'