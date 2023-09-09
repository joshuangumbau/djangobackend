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

from instalments.models import IBSPayer, InstalmentPlan
from instalments.serializer import IBSPayerListSerializer, InstalmentPlanListSerializer
from products.models import Products

class CreateNewuIPSPayerAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request):
        data=request.data
        query=IBSPayer.objects.all()
        serializer=IBSPayerListSerializer(query,many=True).data
        rep_data={
                "status":True,
                "message":"Payers Fethed Successfully",
                "object":serializer
            }
        return Response(rep_data,status=200)
    def post(self,request):
        data = request.data
        print(data)
        payer_code=random.randint(10000,10000000) 
        payer=IBSPayer.objects.filter(email=data["email"]) 
        if (payer.count()==1):
            return Response({
                "status":False,
                "error":"Payer with email Already exist"
            }
            ) 
        created=IBSPayer.objects.create(
                payer_name=data["payer_name"],
                payer_address_code=data["payer_address_code"],
                payer_logo=data["payer_logo"],
                payer_code=payer_code,
                physical_address=data["physical_address"],
                phone=data["phone"],
                email=data["email"],
                logitude=data["logitude"],
                latitude=data["latitude"]
            )
        response=IBSPayerListSerializer(created).data
        rep_data={
            "status":True,
            "message":"Payer Created Successfully",
            "object":response
        }
        return Response(rep_data,status=200)
class EditNewIPSPayerAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request,id):
        data=request.data
        try:
            query=IBSPayer.objects.get(id=id)
            serializer=IBSPayerListSerializer(query).data
            rep_data={
                    "status":True,
                    "message":"Payer Fethed Successfully",
                    "object":serializer
                }
            return Response(rep_data,status=200)
        except:
            rep_data={
                    "status":False,
                    "error":"Payer Does not exist",
                    
                }
            return Response(rep_data)

    def patch(self,request,id):
        data = request.data
        print(data)
        try:
            obj=IBSPayer.objects.get(id=id)  
            obj.payer_name=data["payer_name"]
            obj.payer_address_code=data["payer_address_code"]
            obj.payer_logo=data["payer_logo"]
            obj.physical_address=data["physical_address"]
            obj.phone=data["phone"]
            obj.email=data["email"]
            obj.logitude=data["logitude"]
            obj.latitude=data["latitude"]
            obj.save()
            response=IBSPayerListSerializer(obj).data
            rep_data={
                "status":True,
                "message":"Payer Edited Successfully",
                "object":response
            }
            return Response(rep_data,status=200)
        except:
            rep_data={
                    "status":False,
                    "error":"Payer Does not exist",
                    
                }
            return Response(rep_data)
    def delete(self,request,id):
        data = request.data
        print(data)
        obj=IBSPayer.objects.get(id=id)
        obj.delete()
        rep_data={
                    "status":True,
                    "error":"Payer Deleted Successfully",
                    
                }
        return Response(rep_data)
    

class CreateNewInstalmentAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request):
        data=request.data
        date=datetime.now()
        print(date)
        query=InstalmentPlan.objects.all()
        serializer=InstalmentPlanListSerializer(query,many=True).data
        rep_data={
                "status":True,
                "message":"Instalments Plan Fethed Successfully",
                "object":serializer
            }
        return Response(rep_data,status=200)
    def post(self,request):
        data = request.data
        print(data)
        plan_code=random.randint(10000,10000000) 
        try:
            payer=IBSPayer.objects.get(id=data["payer_id"]) 
        except:
            return Response({
                "status":False,
                "error":"Payer with email does exist"
            }
            ) 
    
        created=InstalmentPlan.objects.create(
                no_of_instalments=data["total_instalments"],
                no_of_first_months=data["down_payment_months"],
                payment_date=data["payment_date"],
                instament_code=plan_code,
                pelnaty_type=data["pelnaty_type"],
                pelnaty_value=int(data["pelnaty_value"])/100 if data["pelnaty_type"] =="Percent" else data["pelnaty_value"]
            )
        
        created.payer=payer
        created.save()
        response=InstalmentPlanListSerializer(created).data
        rep_data={
            "status":True,
            "message":"Instalment Plan Created Successfully",
            "object":response
        }
        return Response(rep_data,status=200)


class EditNewInstalmentPlanAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request,id):
        data=request.data
        try:
            query=InstalmentPlan.objects.get(id=id)
            serializer=InstalmentPlanListSerializer(query).data
            rep_data={
                    "status":True,
                    "message":"Payer Fethed Successfully",
                    "object":serializer
                }
            return Response(rep_data,status=200)
        except:
            rep_data={
                    "status":False,
                    "error":"Payer Does not exist",
                    
                }
            return Response(rep_data)

    def patch(self,request,id):
        data = request.data
        print(data)
        try:
            obj=InstalmentPlan.objects.get(id=id)  
            obj.monthly_fee=data["monthly_fee"]
            obj.initial_fee=data["initial_fee"]
            obj.payment_date=data["payment_date"]
            obj.pelnaty_type=data["pelnaty_type"]
            obj.pelnaty_value=int(data["pelnaty_value"])/100 if data["pelnaty_type"] =="Percent" else data["pelnaty_value"]
            obj.save() 
            response=InstalmentPlanListSerializer(obj).data
            rep_data={
                "status":True,
                "message":"Instalment Plan Edited Successfully",
                "object":response
            }
            return Response(rep_data,status=200)
        except:
            rep_data={
                    "status":False,
                    "error":"Instalment Plan Does not exist",
                    
                }
            return Response(rep_data)
    def delete(self,request,id):
        data = request.data
        print(data)
        obj=InstalmentPlan.objects.get(id=id)
        obj.delete()
        rep_data={
                    "status":True,
                    "error":"Instalment Plan Deleted Successfully",
                    
                }
        return Response(rep_data)