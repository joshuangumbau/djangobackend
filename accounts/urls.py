from django.urls import path,include

from rest_framework import routers

from .views import *
from . import views
from rest_framework.routers import DefaultRouter
rs=DefaultRouter()
urlpatterns = [
        path('login/',login), 
        path('reset_password/',ResetPasswordAPIView.as_view()),
        
        #authentication token paths
        # path('generate_token/', views.generate_token, name= 'generate_token'),
        # path('verify_token/', views.verify_token, name='verify_token'),

        # path('join-chezaaafrica/',JoinChezaaAfrica), 
        # path('users-chezaaafrica/',ChezaaAfricaUsers),
        # path('approve-client/',ChezaaAfricaApprove), 
        # path('decline-client/',ChezaaAfricaDecline), 
        # path('contractuser-auth/',ChezaaAfricaContract),  
        

        path('',include(rs.urls)), 
       
]
