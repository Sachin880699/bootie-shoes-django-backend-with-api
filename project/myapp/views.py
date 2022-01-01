from django.shortcuts import render , HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from.models import *
from rest_framework import viewsets, status, permissions
from.serializers import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import get_user_model
User = get_user_model()

sucess = {'code':status.HTTP_200_OK,'message':'sucess'}
no_argument = {'code':status.HTTP_400_BAD_REQUEST,'message':'no required parameter found'}
failed = {'code':status.HTTP_400_BAD_REQUEST,'message':'failed'}


class UserList(generics.GenericAPIView):
    def get(self , request):
        user_obj = UserData.objects.all().order_by("-id")
        context = {
            "user_list":UserDataSerializer(user_obj,many=True, context={'request': request}).data
        }
        return Response(context)


class SellingItemList(generics.GenericAPIView):
    def get(self , request):
        user_obj = SellingItems.objects.all().order_by("-id")
        context = {
            "user_list":SellingItemsSerializer(user_obj,many=True, context={'request': request}).data
        }
        return Response(context)

class ContactUsView(generics.GenericAPIView):
    def post(self , request):
        data = request.data
        name           = data['name']
        email          = data['email']
        phone_number   = data['phone_number']
        message        = data['message']

        contact_obj = ContactUs.objects.create(
            name             = name,
            email            = email,
            phone_number     = phone_number,
            message          = message
        )
        context = {
            "status":"success",
            
        }
        return Response(context)

class UserLogin(generics.GenericAPIView):
    def post(self , request):
        data        = request.data
        username   = data['username']
        password    = data['password']

        user = auth.authenticate(username=username, password=password)
        

        user_obj = User.objects.get(id = user.id)
        context = {
            "user_data":UserDataSerializer(user_obj,many=False, context={'request': request}).data,
            "username":user_obj.first_name
            
        }
        return Response(context)