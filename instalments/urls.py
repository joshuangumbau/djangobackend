from django.urls import path,include

from rest_framework import routers

from .views import *
from . import views
from rest_framework.routers import DefaultRouter
rs=DefaultRouter()
urlpatterns = [
      
        path('create-new-ibs-payer/',CreateNewuIPSPayerAPIView.as_view()),
        path('edit-new-ibs-payer/<str:id>',views.EditNewIPSPayerAPIView.as_view(),name='EditNewIPSPayerAPIView'),
  
        
        path('create-instalment-plan/',CreateNewInstalmentAPIView.as_view()),
        path('edit-created-instalment-plan/<str:id>',EditNewInstalmentPlanAPIView.as_view(),name='EditNewInstalmentPlanAPIView'),
        path('',include(rs.urls)), ]