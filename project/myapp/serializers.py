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

class SpecialDealOfferSerializer(serializers.ModelSerializer):
    sellingitem = SellingItemsSerializer(read_only=False, many=False)
    class Meta:
        model  = SpecialDealOffer
        fields = '__all__'