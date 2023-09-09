from django.urls import path,include

from rest_framework import routers

from .views import *
from . import views
from rest_framework.routers import DefaultRouter
rs=DefaultRouter()
urlpatterns = [
        path('create-new-kyctemplate/',CreateKYCTemplateAPIView.as_view()),       
        path('edit-single-kyctemplate/<str:id>',views.CRUDKYCTemplateAPIView.as_view(),name='CRUDKYCTemplateAPIView'),


        path('create-new-kyctemplate-section/',CreateKYCTemplateSectionAPIView.as_view()),       
        path('edit-single-kyctemplate-section/<str:id>',views.CRUDKYCTemplateSectionAPIView.as_view(),name='CRUDKYCTemplateSectionAPIView'),

        path('create-new-kyctemplate-subsection/',CreateKYCTemplateSubSectionAPIView.as_view()),       
        path('edit-single-kyctemplate-subsection/<str:id>',views.CRUDKYCTemplateSubSectionAPIView.as_view(),name='CRUDKYCTemplateSubSectionAPIView'),


        path('create-new-question/',CreateQuestionAPIView.as_view()),
        path('edit-single-question/<str:id>',EditQuestionsInaSubSectionAPIView.as_view(),name='EditQuestionsInaSubSectionAPIView'),
        path('get-questions-in-sub-section/<str:id>',QuestionsInaSubSectionAPIView.as_view(),name='QuestionsInaSubSectionAPIView'),
       
       
        path('create-new-question-answers/',CreateQuestionAnswerAPIView.as_view()),
        path('verify-userkyc-documents/',views.VerifyUserDocuments,),
     
       
        path('',include(rs.urls)), ]