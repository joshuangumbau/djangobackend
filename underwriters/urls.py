from django.urls import path,include

from rest_framework import routers

from .views import *
from . import views
from rest_framework.routers import DefaultRouter
rs=DefaultRouter()
urlpatterns = [
      
        path('create-new-underwriters/',CreateNewUnderWritersPIView.as_view()),




       
        path('edit-single-underwriters/<str:id>',views.EditSingleUnderwriter.as_view(),name='EditSingleUnderwriter'),
  
        

        path('',include(rs.urls)), ]