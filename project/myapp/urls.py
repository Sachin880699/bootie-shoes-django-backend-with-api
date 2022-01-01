from django.urls import path
from . import views


urlpatterns = [
    path("UserList",views.UserList.as_view(),name='UserList'),
    path("SellingItemList",views.SellingItemList.as_view() , name = "SellingItemList"),
    path("ContactUsView",views.ContactUsView.as_view() , name = "ContactUsView"),
    path("UserLogin",views.UserLogin.as_view() , name = "UserLogin")
]