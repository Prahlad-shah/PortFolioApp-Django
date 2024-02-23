from django.contrib import admin
from django.urls import path
from .views import (PortFolioView, TestView, ModelNameList, CreateUserView, 
                    UpdateUserView, DeleteUserView)

urlpatterns = [
    path('', PortFolioView.as_view(), name= 'home' ),
    path('testpage', TestView.as_view(), name='register'),
    path('showdata', ModelNameList.as_view(), name='showdata'),
    path('createuser', CreateUserView.as_view(), name='createuser'),
    path('deleteuser/<slug:pk>/', DeleteUserView.as_view(), name='deleteuser'),
    path('updateuser/<slug:pk>/', UpdateUserView.as_view(), name='updateuser'),
]