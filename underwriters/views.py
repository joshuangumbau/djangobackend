import random
from django.shortcuts import render

# Create your views here.
import dataclasses
from datetime import datetime
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView



from django.shortcuts import get_object_or_404

from rest_framework import status, viewsets
from rest_framework.decorators import (api_view, parser_classes,
                                       permission_classes)
from rest_framework.parsers import JSONParser,MultiPartParser,FormParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_302_FOUND, HTTP_400_BAD_REQUEST
from accounts.models import AccountModel
from underwriters.models import Underwriters
from underwriters.serializer import UnderwritersListSerializer



from django.core.mail import EmailMultiAlternatives


class CreateNewUnderWritersPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request):
        data=request.data
        query=Underwriters.objects.filter(is_active=True)
        serializer=UnderwritersListSerializer(query,many=True).data
        rep_data={
                "status":True,
                "message":"Underwriters Fethed Successfully",
                "object":serializer
            }
        return Response(rep_data,status=200)
    def post(self,request):
        data = request.data
        print(data)
        insurer_id=random.randint(10000,10000000)
        
        res=Underwriters.objects.filter(email_id=data["email_id"]).count()
        if(res ==0):
            created=Underwriters.objects.create(
                insurer_name=data["insurer_name"],
                insurer_detail=data["insurer_details"],
                insurer_detail_2=data["insurer_details_2"],
                contact_person=data["contact_person"],
                desgnation=data["desgnation"],
                mobile_number=data["mobile_number"],
                email_id=data["email_id"],
                insurer_id=insurer_id
            )
            created.company_website_url=data["company_website_url"]
            created.latitude=data["latitude"]
            created.longitude=data["longitude"]
            created.profile_url=data["profile_url"]
            created.location_address=data["location_address"]
            created.save()
            created_user=AccountModel.objects.create(
                email=data["email_id"],phone=data["mobile_number"],
                first_name=data["insurer_name"],user_type="Underwriter"
            )
            created_user.set_password(str(insurer_id))
            created_user.save()
            passwordreset=insurer_id
            subject, from_email, to = 'Underwriter Account Created Details', 'thebhubinfor@gmail.com',data['email_id']
           
            text_content = ''
            html_content = """
            <h4>Hi  """ +data['email_id']+""" </h4>
            <div style="margin-left:5px;font-size:12px">
            We have successfully Created your account for the IBS system <a href="https://ibs/bhub/#/login">https://ibs/bhub/#/login</a> <br>
            Below are your Credentials.<br>
            <b>Username</b>: """+data['email_id']+"""<br>
            <b>Password</b>:"""+str(passwordreset)+"""
            <br>
            <br>
            Please Login Using the Above Credentials,<br>
            You can Opt to Reset Your preffered Password  on the Dashboard after Login.<br>
            </div>

            <div>
            Regards,<br>
            Bhub Support,<br>
            
            </div>
            """
            print("tunaanza")
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            print("sending....")
            # print("from":from)
            msg.send()

            response=UnderwritersListSerializer(created).data
            rep_data={
                "status":True,
                "message":"Underwriters Created Successfully",
                "object":response
            }
            return Response(rep_data,status=200)
            
        else:
            rep_data={
                "status":False,
                "message":"Underwriters With Email Id Already Exist",
               
            }
            return Response(rep_data,status=200)
        
class EditSingleUnderwriter(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request,id):
        data=request.data
        try:
            query=Underwriters.objects.get(id=id)
            serializer=UnderwritersListSerializer(query).data
            rep_data={
                    "status":True,
                    "message":"Single Underwriter Fethed Successfully",
                    "object":serializer
                }
            return Response(rep_data,status=200)
        except:
                rep_data={
                    "status":False,
                    "message":"Underwriters Does not exist",
                   
                        }
                return Response(rep_data,status=400)
    def patch(self,request,id):
        data=request.data
        try:
            obj=Underwriters.objects.get(id=id)
            obj.insurer_name=data["insurer_name"]
            obj.insurer_detail=data["insurer_details"]
            obj.insurer_detail_2=data["insurer_details_2"]
            obj.contact_person=data["contact_person"]
            obj.desgnation=data["desgnation"]
            obj.mobile_number=data["mobile_number"]
            try:
                obj.email_id=data["email_id"]
            except:
                pass
            obj.save()

        
            serializer=UnderwritersListSerializer(obj).data
            rep_data={
                    "status":True,
                    "message":"Underwriters Edited Successfully",
                    "object":serializer
                }
            return Response(rep_data,status=200)
        except:
                rep_data={
                    "status":False,
                    "message":"Underwriters Does not exist",
                   
                        }
                return Response(rep_data,status=400)
    def delete(self,request,id):
        data=request.data
        obj=Underwriters.objects.get(id=id)
        obj.delete()
        rep_data={
                    "status":True,
                    "message":"Underwriters Deleted Successfully",
                   
                        }
        return Response(rep_data,status=200)
