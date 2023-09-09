from calendar import monthrange
import datetime
import random
from django.http import JsonResponse
from django.shortcuts import render
from django.db import transaction
from accounts.models import AccountModel
import requests
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from rest_framework.decorators import (api_view, parser_classes,
                                       permission_classes)
from rest_framework.parsers import JSONParser,MultiPartParser,FormParser

from rest_framework.exceptions import NotFound

from dateutil.parser import parse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import api_view,permission_classes
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated,AllowAny

from customers.utilis import convert_phone
from payments.models import MpesaPayment, PushedSTKs
from payments.serializer import MpesaSerialiser

class PushMpesaSTK(APIView):
    permission_classes = [AllowAny,]
    def post(self, request):
        data=request.data
        email=data["email"]
        if (email==''):
             email="dagizo@gmail.com"
        stk_payload={
        'amount': data['amount'],
        'currency': data['currency'],
        'callback_url': data['callback_url'],
        'channel': data['channel'],
        'msisdn': convert_phone(data['msisdn']),
        'phone': convert_phone(data['phone']),
        'email': email
         }
        print(stk_payload)
        url = "https://dev.chedah.io/api/login"
        payload={'email': 'dagizo@gmail.com',
            'password': 'password'}
        files=[]
        auth_headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer 1|52NdZL2gz6G1hS7lE6Ex9ZEM0GWpzJMjikNR7XNR',
        'Cookie': 'XSRF-TOKEN=eyJpdiI6IkI1Q2dMU09iTVFXOEJYaEd5bTVnVGc9PSIsInZhbHVlIjoiMkd1eDZ0cFBXeHY2OVc1dVdQaWx3OG9MTk1sUVdKZjBGYzgxZlJ1MWRVY2tUWGxDaVlRdTdHRERLcmhQV3hSSXplSDVtQitTdEFkRTh1eDNpdDVWSnVRZ1hSamk5b3lnbkNyd0o0R2FNRGg1OGxyckYrLzZNMkdETTEvb2xDWisiLCJtYWMiOiJlZjM5MjljMWMxNjE5MzQwYTZjZGQ4NWUyMzljZjQ3ZWFmZjYwMWJlZTQxMmE3MWY0OTg3NDg1ZDZiOGZjZTk2IiwidGFnIjoiIn0%3D; lipa_session=eyJpdiI6InVoSlFyTVp6N0JFdjNwd29BWlc2S0E9PSIsInZhbHVlIjoiOWZRcXJrSFpZYm4weUE5MkRiU21jdmpVMUtZT252dks5L3ZBbXY2ZkxHSkg0UVJpNDRjWVJheE1ZejJ4a2dpY2JCT09PWGZLZE4xZHQzaGw0UkJCOWx3RG5IUGpQMVpuZ2R4dlp2T1VUQTFqME5XSi9WOU81VXBwSG55ZWIxWG8iLCJtYWMiOiJjN2Q1NGUwMmRkZmNmY2RlMDU0NTZhNWUxZWM3ZjM3MDk3MGU4NTU5ODFhMzk3OTJhYzM5NzA3ZmRmNDY1MjQ0IiwidGFnIjoiIn0%3D'
        }
        response = requests.request("POST", url, headers=auth_headers, data=payload, files=files)
        try:
            obj=json.loads(response.text)
            print("xxxxxxxxxx",response.text)
            access_token=obj['access_token']
            token="Bearer"+" "+access_token 
        except:
             token="Bearer"+" "+"344|59UY3YpkO7L8fA2QRx8sstxdRDcqejrkPueUPCPP"
    #    """ initiate push stk"""
        try:
            stk_url = "https://dev.chedah.io/api/charge"
        
            files=[]
            stk_headers = {
            'Accept': 'application/json',
            'Authorization': token
                    }

            stk_response = requests.request("POST", stk_url, headers=stk_headers, data=stk_payload, files=files)
            stk_data=json.loads(stk_response.text)
            print(stk_data)
            created=PushedSTKs.objects.create(
                    amount=stk_data["amount"],
                    channel=stk_data["channel"],
                    reference=stk_data["reference"],
                    mechant_app_id=stk_data["merchant_app_id"],
                    uuid=stk_data["uuid"],
                    stk_id=stk_data["id"]
            )
            res={
                "response":json.loads(stk_response.text),
                "status":True,
                "message":"stk push was successfull"
            }

            return Response(res,status=200)
        except:
                res={
                "status":False,
                "message":"stk push was not successfull"
                 }

                return Response(res,status=400)

class MpesaCallBack(APIView):
    permission_classes = [AllowAny,]
    def get(self, request):
            data=request.data
            obj=MpesaPayment.objects.all().order_by('-created')
            ser=MpesaSerialiser(obj,many=True)
            res={
                 "status":True,
                 "data":ser.data
            }

            return Response(res)
   

    def post(self, request):
        request_data = json.dumps(request.data)
        data = json.loads(request_data)
        created=MpesaPayment.objects.create(
             phone_number=data['source']['msisdn'],
             email=data['source']['owner_email'],
             amount=data['transaction']['amount'],
             receipt_code =data['transaction']['receipt'],
             channel=data['transaction']['channel'],
             callback_id=data['transaction']['id'],
             charge_id=data['charge_id'],
             status=data['status'],
            
             status_code=data['status_code'],
             date=datetime.datetime.now().date()
                      )
        try:
            created.json_response=data
            created.save()
        except:
             pass

  
        return Response(status=200) 
