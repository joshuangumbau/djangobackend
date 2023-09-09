from django.urls import path,include

from rest_framework import routers

from customers.sms import SMS

# from customers.send_sms import SENDSMS

# from customers.send_sms import make_post_request

from .views import *
from . import views
from rest_framework.routers import DefaultRouter
rs=DefaultRouter()
urlpatterns = [      
        path('create-new-customer-order/',CreateCustomerOrderAPIView.as_view()),
        path('send-client-message/', SMS),


        #policies

        path('ibs-get-allpolicies/',views.GetAllPoliciesAPIView.as_view(),name='GetAllPoliciesAPIView'),
  
        
        # path('create-instalment-plan/',CreateNewInstalmentAPIView.as_view()),
        path('ibs-issue-policy-number/<str:id>',IssuePolicyAPIView.as_view(),name='IssuePolicyAPIView'),
        path('ibs-renew-policy-number/<str:id>',RenewPolicyAPIView.as_view(),name='RenewPolicyAPIView'),
         path('contact-ibs-client/',InboxMessageUserAPIView.as_view(),name='InboxMessageUserAPIView'),
          # path('upload-active-policies/', views.uploadactivepolicies, name='uploadactivepolicies'),
          path('upload-active-policies/',views.AddPatientView.as_view()),

        path('',include(rs.urls)), 
        
        
        ]