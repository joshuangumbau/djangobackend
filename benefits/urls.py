from django.urls import path,include

from rest_framework import routers

from .views import *
from . import views
from rest_framework.routers import DefaultRouter
rs=DefaultRouter()
urlpatterns = [
      
        path('create-new-ibs-taxes/',CreateIBSTaxesAPIView.as_view()),   
        path('edit-single-ibs-tax/<str:id>',views.EditNewIBSTaxAPIView.as_view(),name='EditNewIBSTaxAPIView'),

  
        path('create-ibs-products-terms/',CreateProductTermsAPIView.as_view()),
        path('edit-ibs-products-terms/<str:id>',EditProductTermsAPIView.as_view(),name='EditProductTermsAPIView'),
        path('create-product-benefit/<str:id>',CreateProductBenefitsAPIView.as_view(),name='CreateProductBenefitsAPIView'),
        path('create-motor-product-benefit/<str:id>',CreateMotorProductBenefitsAPIView.as_view(),name='CreateMotorProductBenefitsAPIView'),
        path('create-product-benefit-details/<str:id>',CreateProductBenefitsDetailsAPIView.as_view(),name='CreateProductBenefitsDetailsAPIView'),
        path('create-motor-product-benefit-detail/<str:id>',views.CreateMotorProductBenefitsDetailsAPIView.as_view(),name='CreateMotorProductBenefitsDetailsAPIView'),
        path('edit-product-benefit-class/<str:id>',EditBenefitClassAPIView.as_view(),name='EditBenefitClassAPIView'),
        path('edit-product-benefit-detail/<str:id>',EditBenefitDetailsAPIView.as_view(),name='EditBenefitDetailsAPIView'),
        path('get-product-benefits-details/',views.GetBenefitDetailsAPIView),
        path('link-product-to-tax/<str:id>',views.LinkTaxToProductAPIView.as_view(),name='LinkTaxToProductAPIView'),
        path('link-product-to-terms/<str:id>',views.LinkTermsToProductAPIView.as_view(),name='LinkTermsToProductAPIView'),
        path('link-product-to-kyc/<str:id>',views.LinkKYCToProductAPIView.as_view(),name='LinkKYCToProductAPIView'),
        path('create-age-groups/',views.AgeRangeAPIView.as_view(),name='AgeRangeAPIView'),
        path('edit-age-groups/<str:id>',views.EditAgeRangeAPIView.as_view(),name='EditAgeRangeAPIView'),
        path('create-inclusive-package/',views.CreateOtherPackageAPIView.as_view(),name='CreateOtherPackageAPIView'),

        path('create-inclusive-package-details/',views.CreateOtherPackageDetailsAPIView.as_view(),name='CreateOtherPackageDetailsAPIView'),
        path('create-provider-details/',views.CreateNewProviderAPIView.as_view(),name='CreateNewProviderAPIView'),
        path('edit-provider-details/<str:id>',views.EditProviderDetailsAPIView.as_view(),name='EditProviderDetailsAPIView'),
        path('create-specialist-details/',views.CreateNewSpecialistAPIView.as_view(),name='CreateNewSpecialistAPIView'),
        path('edit-specialist-details/<str:id>',views.EditSpecialistDetailsAPIView.as_view(),name='EditSpecialistDetailsAPIView'),
        path('',include(rs.urls)), ]