from django.urls import path,include

from rest_framework import routers

from .views import *
from . import views
from rest_framework.routers import DefaultRouter
rs=DefaultRouter()
urlpatterns = [
        path('mpesa-pushstk/', views.PushMpesaSTK.as_view(), name='PushMpesaSTK'),

        path('mpesapayments/callback/', views.MpesaCallBack.as_view(), name='MpesaCallBack'),

        path('',include(rs.urls)), ]