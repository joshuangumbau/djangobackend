from django.urls import path,include

from rest_framework import routers

from .views import *
from . import views
from rest_framework.routers import DefaultRouter
rs=DefaultRouter()
urlpatterns = [
        #create apis
      
        path('create-new-products/',CreateNewuctsAPIView.as_view()),
        path('display-all-products/',views.KatabimaProductsAPIView.as_view()),
        path('create-products-policy-class/',CreateNewPolicyClassAPIView.as_view()),
        path('create-products-policy-type/',views.CreateNewPolicyTypeClassAPIView.as_view()),
        path('create-products-policy-type-category/',views.CreateProductCategoryAPIView.as_view()),
        #edit apis
        path('edit-single-products/<str:id>',views.EditSingleProductAPIView.as_view(),name='EditSingleProductAPIView'),
        path('edit-single-products-policy-class/<str:id>',EditSingleProductPolicyAPIView.as_view(),name='EditSingleProductAPIView'),
        path('edit-single-products-policy-type/<str:id>',EditSingleProductPolicyTypeAPIView.as_view(),name='EditSingleProductAPIView'),
        path('edit-products-policy-type-category/<str:id>',views.EditProductCategoryAPIView.as_view()),
        #general aapis
        path('get-policy-types-in-class/<str:id>',views.GetAllTypesInCategoryAPIView.as_view()),
        path('get-policy-categories-in-types/<str:id>',views.GetAllCategoryinTypesAPIView.as_view()),
        path('get-dashboard-report/' ,views.GetDashboardReportAPIView.as_view()),

        #excell formats downloads
        path('providers-sample-download/',ProvidersSampleUploadExcelView.as_view()),
        path('specialists-sample-download/',SpecialistSampleUploadExcelView.as_view()),
        path('upload-specialist-data/',views.UploadSpecialistView.as_view()),
          path('upload-provider-data/',views.UploadProvidersView.as_view()),

        path('',include(rs.urls)), ]