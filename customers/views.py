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
from benefits.models import BenefitDetails, ProductBenefits

from customers.models import  CustomerOrder, Policies
from customers.serializer import CustomerListSerializer, policyListSerializer
from customers.utilis import convert_phone
from instalments.models import IBSPayer
from products.models import Products
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse
import africastalking                                                                                                                                                                                          

class CreateCustomerOrderAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request):
        data=request.data
        query=CustomerOrder.objects.all()
        dt=CustomerListSerializer(query).data
        rep_data={
                "status":True,
                "message":"Taxes Fethed Successfully",
                "object":dt
            }
        return Response(rep_data,status=200)
    def post(self,request):
        data = request.data
        print(data)
        order=random.randint(10000,10000000)
        order_no="#"+str(order)

        try:
            product=Products.objects.get(id=data["product_id"])
        except:
             return Response({
                "status":False,
                "error":"The product id   does not exist"
            },status=400)
        try:
            benefits=ProductBenefits.objects.get(id=data["benefit_id"])
        except:
             return Response({
                "status":False,
                "error":"The benefit does not exist"
            },status=400)
        try:
            benefit_details=BenefitDetails.objects.get(id=data["benefit_detail_id"])
        except:
             return Response({
                "status":False,
                "error":"The benefit details does not exist"
            },status=400)
       

        created,obj=AccountModel.objects.update_or_create(
             email=data["email"],
            phone=data["phone"],
            defaults={
                 'first_name':data["first_name"],
                'last_name':data["surname"],
                'gender':data["gender"],
                ' user_type':data["user_type"]
            }     
            )                      
        created.set_password(str(order))
        created.save()
        POLICICY=random.randint(100000,10000000)
      
        user_obj=CustomerOrder.objects.create(
            order_number=order_no,
            product=product,
            benefit=benefits,
            benefit_details=benefit_details,
            user=created,
            order_amount=data["order_amount"]

        )
        # period_id
        policy=Policies.objects.create(
            client=created,
            product=product,
            benefit=benefits,
            benefit_details=benefit_details,
            policy_number="INT-POL-NO"+str(order_no)+"/"+str(POLICICY),
            document_no="DN-"+str(order_no),
            policy_amount=data["order_amount"]
        )
        dt=CustomerListSerializer(user_obj).data
        rep_data={
            "status":True,
            "message":"user order Created Successfully",
            "data":dt
            
        }
        return Response(rep_data,status=200)
    

class GetAllPoliciesAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request):
        data=request.data
        query=Policies.objects.all()
        dt=policyListSerializer(query,many=True).data
        rep_data={
                "status":True,
                "message":"policies Fethed Successfully",
                "count":query.count(),
                "policy":dt
            }
        return Response(rep_data,status=200)

class IssuePolicyAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def post(self,request,id):
        data=request.data
        try:
            obj=Products.objects.get(id=data["product_id"])
        except:
            return Response({
             "status":False,
             "error":"product with that id does not exis t"   
            })            
                                              
        try:

            policy=Policies.objects.get(id=id)
        except:
             return Response({
             "status":False,
             "error":"policy with that id does not exist"   
            }) 
        period=obj.active_period
        if (period >=1):
            one=random.randint(10000,10000000)
            two=random.randint(1000,1000000)
            print(period)
            today=datetime.today()
            month=today.month
            year=today.year
            print(today)
            policy_no="0"+str(month)+"/"+"POL"+"/"+str(one)+"/"+str(two)+"/"+str(year)
            print(policy_no)
            f=today+relativedelta(months=period)
            print("printing f",f)                        
            policy.status="Active"
            policy.start_date=today
            policy.expiry=f
            policy.end_date=f
            policy.policy_number=policy_no
            policy.save()
            ser=policyListSerializer(policy).data
            sms_number=convert_phone(data["user_phone"])
            username = "katabima"    
            api_key = "eb5095975a73fdce7f8be9c8b29d4b750c53be89e75e376589f0eb9d50c8deb5"    
            africastalking.initialize(username, api_key)
            sms = africastalking.SMS
            message="Congratulations. Your insurance cover with  PACIFIC INSURANCE BROKERS has been approved and your policy number is "+policy_no+" Kindly note it will expire on "+f.strftime("%d %B, %Y")
            response = sms.send(message, [sms_number])
            print(response)
            resp={
                "status":True,
                "message":"Policy number assigned successfully",
                "policy":ser
            }
            
            return Response(resp,status=200)
        else:
            return Response(
               { "status":False,
                "error":"policy period is not set on the product"}
            )
        

class RenewPolicyAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def post(self,request,id):
        data=request.data
        try:
            obj=Products.objects.get(id=data["product_id"])
        except:
            return Response({
             "status":False,
             "error":"product with that id does not exis t"   
            })            
                                              
        try:

            policy=Policies.objects.get(id=id)
        except:
             return Response({
             "status":False,
             "error":"policy with that id does not exist"   
            }) 
        period=obj.active_period
        if (period >=1):
            print(period)
            today=datetime.today()
            print(today)
            f=today+relativedelta(months=period)
            print("printing f",f)                        
            policy.status="Active"
            policy.start_date=today
            policy.business_type="Renewal"
            policy.expiry=f
            policy.end_date=f
            policy.save()
            ser=policyListSerializer(policy).data
            sms_number=convert_phone(data["user_phone"])
            username = "katabima"    
            api_key = "eb5095975a73fdce7f8be9c8b29d4b750c53be89e75e376589f0eb9d50c8deb5"    
            africastalking.initialize(username, api_key)
            sms = africastalking.SMS
            message="Congratulations. Your insurance cover with  PACIFIC INSURANCE BROKERS has been Renewed successfully Kindly note it will expire on "+f.strftime("%d %B, %Y")
            response = sms.send(message, [sms_number])
            print(response)
            resp={
                "status":True,
                "message":"Policy number assigned successfully",
                "policy":ser
            }
            
            return Response(resp,status=200)
        else:
            return Response(
               { "status":False,
                "error":"policy period is not set on the product"}
            )
        

class InboxMessageUserAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def post(self,request):
        data=request.data
        username = "katabima"    
        api_key = "eb5095975a73fdce7f8be9c8b29d4b750c53be89e75e376589f0eb9d50c8deb5"    
        africastalking.initialize(username, api_key)
        sms = africastalking.SMS
        message=data["message"]
        phone=data["user_phone"]
        sms_number=convert_phone(phone)
        response = sms.send(message, [sms_number])
        print(response)
        resp={
                "status":True,
                "message":"message successfully send"
            }
        return Response(resp,status=200)                                                                          
            

from xlrd import open_workbook,xldate 
import xlrd
import openpyxl
import base64
import os
from django.core.files.storage import default_storage

# @api_view(['POST'])
# @permission_classes((AllowAny,))
# @parser_classes((JSONParser,FormParser,MultiPartParser ))
# def uploadactivepolicies(request):
#     data=request.data
#     print(data)
#     # if "GET" == request.method:
#     #     return render(request, 'myapp/index.html', {})
#     # else:
#     excel_file = request.FILES["excel_file"]
#     with open(default_storage.path(data["filename"]), 'wb') as f:
                        
#         f.write(excel_file.read().decode())

#         file_path = os.path.join('media', data['filename'])
#         # myfile=base64.b64decode(str(data['file']).replace('data:application/vnd.ms-excel;base64,',''))
#         print(data['filename'])
#         files = {open(file_path, 'rb')}

#         wb = open_workbook(default_storage.path(data['filename']))
#         print(wb)
        
#         worksheet = wb.sheets()[0]
        
#         print(worksheet)
#         excel_data = list()
#         for row in worksheet.iter_rows():
#             print("this is the point")
#             print(row)
#             row_data = list()
#             for cell in row:
#                 print(cell)
#                 row_data.append(str(cell.value))
# import io
# import pandas as pd
# @api_view(['POST'])
# @permission_classes((AllowAny,))
# def  uploadactivepolicies(request):
#     if request.method == 'POST':

#             excel_file = request.FILES['excel'].read()

#             data = pd.read_excel(io.BytesIO(excel_file))

#             for  row in data.iterrows():
#                 # print(row[0:1])
#                 # print(row[0:2])
#                 print(row[3:3])
#                 print(row.get("date"))


#             return Response("Invalid request method")


class AddPatientView(APIView):
        parser_classes = (MultiPartParser,JSONParser)
        permission_classes=[IsAuthenticated]
        def post(self,request): 


                data = request.data
                file=request.FILES['excel'].read()
                base64_encoded = base64.b64encode(file).decode('UTF-8')
                print(base64_encoded)
                
               
                with open(default_storage.path(data['filename']), 'wb') as f:
                        
                        f.write(base64.b64decode(str(base64_encoded).replace('data:application/vnd.ms-excel;base64,','')))
        
                file_path = os.path.join('media', data['filename'])
                # myfile=base64.b64decode(str(data['file']).replace('data:application/vnd.ms-excel;base64,',''))
                print(data['filename'])
                files = {open(file_path, 'rb')}
        
                wb = open_workbook(default_storage.path(data['filename']))
                print(wb)
                
                worksheet = wb.sheets()[0]
                
                print(worksheet)
                excel_data = list()
                
                for row in range(0, worksheet.nrows):
                    document_number=worksheet.cell_value(row, 0)
                    print(document_number)
                    date=worksheet.cell_value(row, 1)
                    policy_number=worksheet.cell_value(row, 2)
                    business_type=worksheet.cell_value(row, 3)
                    client_code=worksheet.cell_value(row, 4)
                    client_group=worksheet.cell_value(row, 6)
                    client_name=worksheet.cell_value(row, 5)
                    insurer_code=worksheet.cell_value(row, 7)
                    insurer_name=worksheet.cell_value(row, 8)
                    policy_type=worksheet.cell_value(row, 9)
                    premium=worksheet.cell_value(row, 10)
                    # start_date=worksheet.cell_value(row, 28)
                    # end_date=worksheet.cell_value(row, 29)
                    client_totals=worksheet.cell_value(row, 31)
                    requested_by=worksheet.cell_value(row, 34)
                    currency=worksheet.cell_value(row, 36)
                    approved_by=worksheet.cell_value(row, 35)
                    # sum_insured=worksheet.cell_value(row, 40)
                    em=str(client_code)+"@gmail.com"
                    try:
                        name=str(client_name).split()
                        first_name=name[0]
                    except:
                         pass
                    try:
                        lastname=name[1]
                    except:
                         lastname=""
                    try:
                                start_date = xlrd.xldate_as_datetime(worksheet.cell_value(row, 27),27)
                        
                    except:
                                try:
                                       start_date = parse(worksheet.cell_value(row, 27).strip().encode('utf-8'))
                                       print(start_date)
                                except:
                                        start_date="2022-07-26 00:00:00"
                    try:
                                end_date = xlrd.xldate_as_datetime(worksheet.cell_value(row, 28),28)
                        
                    except:
                                try:
                                       end_date = parse(worksheet.cell_value(row, 28).strip().encode('utf-8'))
                                       print(start_date)
                                except:
                                        end_date="2022-07-26 00:00:00"

                    created,oj=AccountModel.objects.get_or_create(email=em,
                      defaults={
                           "client_code":client_code,
                    "first_name":first_name,"last_name":lastname
                      }
                    
                    )
                    payer,obj=IBSPayer.objects.get_or_create(
                         payer_code=insurer_code,
                         defaults={
                              "payer_name":insurer_name
                         }
                         
                    )

                    policies_upload=Policies.objects.update_or_create(
                        policy_number=policy_number ,
                        defaults={                   
                        'document_no':document_number,
                        "start_date":start_date,
                        "end_date":end_date,
                        "expiry":end_date,
                        "policy_amount":premium,
                        "business_type":business_type,
                        "policy_type" : policy_type,
                        "client_group":client_group,
                        "client":created,
                        "approved_by":approved_by,
                        "requested_by":requested_by,
                        "payer":payer,
                        "currency":currency

                        })
                    resp={
                         "status":True,
                         "message":"The policies was successfully uploaded",
                         "total policies":Policies.objects.all().count()
                    }
                return Response(resp,status=200)
                        
      