from django.shortcuts import render


import dataclasses
from datetime import datetime
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
import random


from django.shortcuts import get_object_or_404

from rest_framework import status, viewsets
from rest_framework.decorators import (api_view, parser_classes,
                                       permission_classes)
from rest_framework.parsers import JSONParser,MultiPartParser,FormParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_302_FOUND, HTTP_400_BAD_REQUEST
from KYC.models import KYCTemplate, KYCTemplateSection, KYCTemplateSubSection, KycAnswersModel, SubSectionQuestions
from KYC.serializer import AnswersListSerializer, KYCTemplatSubSectionListSerializer, KYCTemplateListSerializer, KYCTemplateSectionListSerializer, SubSectionQuestionsAnswersListSerializer, SubSectionQuestionsListSerializer
from accounts.models import AccountModel
from accounts.serializer import UserSerializer
from products.models import Products


"""
KYCTEMPLATE OPERATIONS CREATED FIRST THEN THE SECTION FOLLOWS ON THE NEXT COMMENT SECTION

"""

class CreateKYCTemplateAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request):
        data=request.data
        query=KYCTemplate.objects.filter()
        serializer=KYCTemplateListSerializer(query,many=True).data
        rep_data={
                "status":True,
                "message":"KYCTemplate Fethed Successfully",
                "object":serializer
            }
        return Response(rep_data,status=200)
    def post(self,request):
        data = request.data
        print(data)
        kyc_number=random.randint(1000,100000000)
       
        try:
            organization=AccountModel.objects.get(email=data["user_email"])
        except:
            return Response({
                "status":False,
                "error":"Organization creating this kyctemplate is not defined"
            })
        
        duplicate= KYCTemplate.objects.filter(kyc_name__iexact=data["kyc_name"])
        if duplicate.exists():
            return Response({
                "status":False,
                "error":"Tempate already Exists"
            },status=400)
        created=KYCTemplate.objects.create(
                kyc_name=data["kyc_name"],
                description=data["kyc_description"],
                kyctemplate_number=kyc_number,
                organization=organization
                
            )
        response=KYCTemplateListSerializer(created).data
        rep_data={
            "status":True,
            "message":"KycTemplate Created Successfully",
            "object":response
        }
        return Response(rep_data,status=200)
class CRUDKYCTemplateAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request,id):
        data=request.data
        print(data)
        try:
            query=KYCTemplate.objects.get(id=id)
            serializer=KYCTemplateListSerializer(query).data
            rep_data={
                    "status":True,
                    "message":"KYCTemplate Fethed Successfully",
                    "object":serializer
                }
            return Response(rep_data,status=200)
        except:
            rep_data={
                    "status":False,
                    "error":"KYCTemplate With Id does not Exist",
                  
                }
            return Response(rep_data,status=400)
    def patch(self,request,id):
        data=request.data
        try:
            obj=KYCTemplate.objects.get(id=id)
            obj.kyc_name=data["kyc_name"]
            obj.description=data["kyc_description"]
            serializer=KYCTemplateListSerializer(obj).data
            rep_data={
                    "status":True,
                    "message":"KYCTemplate edited Successfully",
                    "object":serializer
                }
            return Response(rep_data,status=200)
        except:
            rep_data={
                    "status":False,
                    "error":"KYCTemplate With Id does not Exist",
                  
                }
            return Response(rep_data,status=400)
    def delete(self,request,id):
        data=request.data
        try:
            obj=KYCTemplate.objects.get(id=id)
            obj.delete()
            rep_data={
                    "status":True,
                    "message":"KYCTemplate deleted Successfully",
                }
            return Response(rep_data,status=200)
        except:
            rep_data={
                    "status":False,
                    "error":"KYCTemplate With Id does not Exist",
                  
                }
            return Response(rep_data,status=400)
        

       
"""
CREATING KYC SECTIONS FOLLOWS HERE WITH THE SUBSECTION ON NEXT COMMENT SECTION

"""



class CreateKYCTemplateSectionAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request):
        data=request.data
        query=KYCTemplateSection.objects.all()
        serializer=KYCTemplateSectionListSerializer(query,many=True).data
        rep_data={
                "status":True,
                "message":"KYCTemplateSections Fethed Successfully",
                "object":serializer
            }
        return Response(rep_data,status=200)
    def post(self,request):
        data = request.data
        print(dataclasses)
        
        section_number=random.randint(1000,100000000)
        try:
            kyc=KYCTemplate.objects.get(id=data["kyc_id"])
        except:
            return Response({
                "status":False,
                "error":"Template to link this section does not exist"
            })
    
        
        duplicate= KYCTemplateSection.objects.filter(section_name__iexact=data["section_name"])
        if duplicate.exists():
            return Response({
                "status":False,
                "error":"Section already Exists"
            },status=400)
        created=KYCTemplateSection.objects.create(
                section_name=data["section_name"],
                section_number=section_number,
                template=kyc
                
            )
        response=KYCTemplateSectionListSerializer(created).data
        rep_data={
            "status":True,
            "message":"KycTemplateSection Created Successfully",
            "object":response
        }
        return Response(rep_data,status=200)
    

class CRUDKYCTemplateSectionAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request,id):
        data=request.data
        print(data)
        try:
            query=KYCTemplateSection.objects.get(id=id)
            serializer=KYCTemplateSectionListSerializer(query).data
            rep_data={
                    "status":True,
                    "message":"KYCTemplateSection Fethed Successfully",
                    "object":serializer
                }
            return Response(rep_data,status=200)
        except:
            rep_data={
                    "status":False,
                    "error":"KYCTemplateSection With Id does not Exist",
                  
                }
            return Response(rep_data,status=400)
    def patch(self,request,id):
        data=request.data
        try:
            obj=KYCTemplateSection.objects.get(id=id)
            obj.section_name=data["section_name"]
            obj.save()
          
            serializer=KYCTemplateSectionListSerializer(obj).data
            rep_data={
                    "status":True,
                    "message":"KYCTemplateSection edited Successfully",
                    "object":serializer
                }
            return Response(rep_data,status=200)
        except:
            rep_data={
                    "status":False,
                    "error":"KYCTemplateSection With Id does not Exist",
                  
                }
            return Response(rep_data,status=400)
    def delete(self,request,id):
        data=request.data
        try:
            obj=KYCTemplateSection.objects.get(id=id)
            obj.delete()
            rep_data={
                    "status":True,
                    "message":"KYCTemplateSection deleted Successfully",
                }
            return Response(rep_data,status=200)
        except:
            rep_data={
                    "status":False,
                    "error":"KYCTemplateSection With Id does not Exist",
                  
                }
            return Response(rep_data,status=400)
        

"""

CREATING KYC SUBSECTIONS FOLLOWS HERE WITH THE QUESTION ENDPOINTS DEFINED IN THE NEXT COMMENT SECTION

"""

class CreateKYCTemplateSubSectionAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request):
        data=request.data
        query=KYCTemplateSubSection.objects.all()
        serializer=KYCTemplatSubSectionListSerializer(query,many=True).data
        rep_data={
                "status":True,
                "message":"KYCTemplateSubSections Fethed Successfully",
                "object":serializer
            }
        return Response(rep_data,status=200)
    def post(self,request):
        data = request.data
        print(dataclasses)
        
        sub_section_number=random.randint(1000,100000000)
        try:
            section=KYCTemplateSection.objects.get(id=data["section_id"])
        except:
            return Response({
                "status":False,
                "error":"SectionTemplate to link this Subsection does not exist"
            })
    
        
        duplicate= KYCTemplateSubSection.objects.filter(sub_section_name__iexact=data["sub_section_name"])
        if duplicate.exists():
            return Response({
                "status":False,
                "error":"subSection already Exists"
            },status=400)
        created=KYCTemplateSubSection.objects.create(
                sub_section_name=data["sub_section_name"],
                subsection_number=sub_section_number,
                section=section
                
            )
        response=KYCTemplatSubSectionListSerializer(created).data
        rep_data={
            "status":True,
            "message":"KycTemplatesubSection Created Successfully",
            "object":response
        }
        return Response(rep_data,status=200)
    

class CRUDKYCTemplateSubSectionAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request,id):
        data=request.data
        print(data)
        try:
            query=KYCTemplateSubSection.objects.get(id=id)
            serializer=KYCTemplatSubSectionListSerializer(query).data
            rep_data={
                    "status":True,
                    "message":"KYCTemplatesubSection Fethed Successfully",
                    "object":serializer
                }
            return Response(rep_data,status=200)
        except:
            rep_data={
                    "status":False,
                    "error":"KYCTemplateSubSection With Id does not Exist",
                  
                }
            return Response(rep_data,status=400)
    def patch(self,request,id):
        data=request.data
        try:
            obj=KYCTemplateSubSection.objects.get(id=id)
            obj.sub_section_name=data["sub_section_name"]
            obj.save()
          
            serializer=KYCTemplatSubSectionListSerializer(obj).data
            rep_data={
                    "status":True,
                    "message":"KYCTemplateSubSection edited Successfully",
                    "object":serializer
                }
            return Response(rep_data,status=200)
        except:
            rep_data={
                    "status":False,
                    "error":"KYCTemplatesubSection With Id does not Exist",
                  
                }
            return Response(rep_data,status=400)
    def delete(self,request,id):
        data=request.data
        try:
            obj=KYCTemplateSubSection.objects.get(id=id)
            obj.delete()
            rep_data={
                    "status":True,
                    "message":"KYCTemplateSubSection deleted Successfully",
                }
            return Response(rep_data,status=200)
        except:
            rep_data={
                    "status":False,
                    "error":"KYCTemplateSubSection With Id does not Exist",
                  
                }
            return Response(rep_data,status=400)

"""

CREATE QUESTIONS FOLLOWS IN THE COMMENT SECTION HERE 

"""

class CreateQuestionAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request):
        data=request.data
        query=SubSectionQuestions.objects.filter()
        serializer=SubSectionQuestionsListSerializer(query,many=True).data
        rep_data={
                "status":True,
                "message":"Questions Fethed Successfully",
                "object":serializer
            }
        return Response(rep_data,status=200)
    def post(self,request):
        data = request.data
        print(data)
        question_number=random.randint(1000,100000000)
        try:
            section=KYCTemplateSection.objects.get(id=data["section_id"])
        except:
            return Response({
                "status":False,
                "error":"section with that id does not Exist"
            },status=400)
        # try:
        #     sub_section=KYCTemplateSubSection.objects.get(id=data["sub_section_id"])
        # except:
        #     return Response({
        #         "status":False,
        #         "error":"sub section with that id does not Exist"
        #     },status=400)
        # try:
        #     kyc=KYCTemplate.objects.get(id=section.id)
        #     print(kyc)
        # except:
        #     return Response({
        #         "error":"The section is not well linked to the Kyc Template"
        #     })
        print("kyc id",section.template.id)
        try:
            template=KYCTemplate.objects.get(id=section.template.id)
        except:
            return Response({
                "status":False,
                "error":"Kyc section not well linked to Template"},status=400)

        created=SubSectionQuestions.objects.create(
                field_type=data["field_type"],
                question_name=data["question_name"],
                question_number=question_number,
                defaults=data["defaults"],
                # sub_section=sub_section
                
            )
        created.template=template
        created.section=section
        created.save()
        response=SubSectionQuestionsListSerializer(created).data
        rep_data={
            "status":True,
            "message":"Question Created Successfully",
            "object":response
        }
        return Response(rep_data,status=200)
    
class QuestionsInaSubSectionAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[AllowAny]
    def get(self,request,id):
        data=request.data
        try:
            sub_section=KYCTemplateSubSection.objects.get(id=id)
        except:
            return Response({
                "status":False,
                "error":"Sub section with this id does not Exist"
            },status=400)
        query=SubSectionQuestions.objects.filter(sub_section=sub_section)
        serializer=SubSectionQuestionsListSerializer(query,many=True).data
        rep_data={
                "status":True,
                "message":"SubSectionQuestionsList Fethed Successfully",
                "object":serializer
            }
        return Response(rep_data,status=200)
class EditQuestionsInaSubSectionAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request,id):
        data=request.data
        try:
            question=SubSectionQuestions.objects.get(id=id)
            serializer=SubSectionQuestionsListSerializer(question).data
            rep_data={
                "status":True,
                "message":"Question Fethed Successfully",
                "object":serializer
            }
            return Response(rep_data,status=200)
        except:
            return Response({
                "status":False,
                "error":"Question with this id does not Exist"
            },status=400)
    def patch(self,request,id):
        data=request.data
        try:
            obj=SubSectionQuestions.objects.get(id=id)
            obj.question_name=data["question_name"]
            obj.field_type=data["field_type"]
            obj.defaults=data["defaults"]
            obj.save()
            ser=SubSectionQuestionsListSerializer(obj).data
            return Response(
                {
                    "status":True,
                    "message":"Edit Was Successfully",
                    "data":ser
                }
            )
        except:
            return Response({
                "status":False,
                "error":"Question with this id does not Exist"
            },status=400)
        

    def delete(self,request,id):
        data=request.data
        try:
            obj=SubSectionQuestions.objects.get(id=id)
            obj.delete()
            return Response({
                "status":True,
                "message":"deletion was successfull"
            })
            
        except:
            return Response({
                "status":False,
                "error":"Question with this id does not Exist"
            },status=400)


"""

CREATE ANSWERS FOR THE SET KYC QUESTIONS AND ONBOARDING OF THE NEW  SYSTEM USERS

"""


class CreateQuestionAnswerAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def post(self,request,*args, **kwargs):
        data=request.data
        for n in data["answers"]:
                print(n)
                try:
                    user=AccountModel.objects.get(email=n["user_email"])
                except:
                    return Response(
                        {
                        "status":False,
                        "error":"The user with the email does  not Exist"
                        })
                try:
            
     
                    question=SubSectionQuestions.objects.get(id=n["question_id"])
                except:
                    return Response(
                        {
                        "status":False,
                        "error":"The Question with the id does  not Exist"
                        })
                try:
                    obj_section=KYCTemplateSection.objects.get(id=n["section_id"])
                except:
                        return Response(
                            {
                            "status":False,
                            "error":"Section with the id does  not Exist"
                            })
        
                created=KycAnswersModel.objects.create(
                    subsection_id=n["generated_subsection_id"],
                    client=user,
                    question=question,
                    section=obj_section,
                    answer=n["answer"],
                    product_id=n["product_id"]

            
                    )
        return Response(
                {
                "status":True,
                "message":"Ansers were created Successfully",
                })



            

        
@api_view(['GET'])
@permission_classes((AllowAny,))
@parser_classes((JSONParser,FormParser,MultiPartParser ))
def  VerifyUserDocuments(request):
        user=request.query_params.get('user_id')
        product=request.query_params.get('product_id')

        try:
            user_id=AccountModel.objects.get(id=user)
        except:
            return Response({
                "status":False,
                "error":"user with the id does not exist"
            })

        query=KycAnswersModel.objects.filter(client=user_id,product_id=product)
        answer_serializer=AnswersListSerializer(query,many=True).data
        user_serializer=UserSerializer(user_id).data

        resp={
            "status":True,
            "message":"document fetched successfully",
            "user":user_serializer,
            "data":answer_serializer
        }
        return Response(resp,status=200)
