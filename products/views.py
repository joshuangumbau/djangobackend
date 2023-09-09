import random
from django.shortcuts import render

# Create your views here.
import dataclasses
from datetime import datetime, timedelta

from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions
from rest_framework.views import APIView

from django.http.response import HttpResponse
from django.db.models import Count, Sum
import xlwt

from django.shortcuts import get_object_or_404

from rest_framework import status, viewsets
from rest_framework.decorators import (api_view, parser_classes,
                                       permission_classes)
from rest_framework.parsers import JSONParser,MultiPartParser,FormParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_302_FOUND, HTTP_400_BAD_REQUEST
from KYC.models import KYCTemplate
from benefits.models import AgeSetup, BulkPlanBenefit, ProductProvider, ProductSpecialist, ProductTaxes, ProductTerms, Provider, Specialist, Taxes, Terms
from benefits.serializer import BulkPlanBenefitsListSerializer, ProductTaxesListSerializer, ProductTermsListSerializer
from customers.models import Policies
from instalments.models import IBSPayer, InstalmentPlan
from payments.models import MpesaPayment

from products.models import PolicyTypeCategory, ProductIPFDetail, ProductPolicyClass, ProductPolicyType, Products
from products.serializer import CategoryListSerializer, IPFProviderListSerializer, ProductPolicyClassListSerializer, ProductPolicyClasstypeListSerializer, ProductsListSerializer, ProviderListSerializer, SpecialistListSerializer
from underwriters.models import Underwriters
from xlrd import open_workbook,xldate 
import xlrd
import openpyxl
import base64
import os
from django.core.files.storage import default_storage


class CreateNewuctsAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request):
        data=request.data
        query=Products.objects.filter(is_active=True)
        serializer=ProductsListSerializer(query,many=True).data
        rep_data={
                "status":True,
                "message":"Products Fethed Successfully",
                "object":serializer
            }
        return Response(rep_data,status=200)
    def post(self,request):
        data = request.data
        resp_data=[]
        print(data["product_details"]["terms_id"])


        try:
            policyclass=ProductPolicyClass.objects.get(id=data["product_details"]["product_class_id"])
        except:
            return Response({
                "status":False,
                "error":"the policy class with the ID does not exist"
            },status=400)
        try:
            policytype=ProductPolicyType.objects.get(id=data["product_details"]["policy_type_id"])
        except:
            return Response({
                "status":False,
                "error":"the policy type with the ID does not exist"
            },status=400)
        try:
            underwriter=Underwriters.objects.get(id=data["product_details"]["underwriter_id"])
        except:
            return Response({
                "status":False,
                "error":"The Underwriter  with the id does not exist"
            },status=400)
        try:
            kyc=KYCTemplate.objects.get(id=data["product_details"]["kyc_id"])
        except:
            return Response({
                "status":False,
                "error":"The kyc  with the id does not exist"
            },status=400)
        try:
            product_terms=Terms.objects.get(id=data["product_details"]["terms_id"])
        except:
            return Response({
                "status":False,
                "error":"The Terms with  the id does not exist"
            },status=400)
        product_number=random.randint(10000,10000000)
        created_product=Products.objects.create(
                product_name=data["product_details"]["product_name"],
                product_description=data["product_details"]["product_description"],
                product_number=product_number,
                product_image_url=data["product_details"]["product_image_url"],
                broker_commission=data["product_details"]["broker_commission"],
                active_period=data["product_details"]["active_period"],
                is_financed=(data["ipf_provider"]["is_financed"]).lower()
            )
        created_product.status="NEW"  
        created_product.policy_class=policyclass
        created_product.underwriter=underwriter
        created_product.policy_type=policytype
        created_product.kyc=kyc
        created_product.save()
 
        product_term=ProductTerms.objects.update_or_create(
            product=created_product,term=product_terms
                )
        for a in data["product_tax"]:
            taxation=Taxes.objects.get(id=a["tax_id"])
            product_taxes=ProductTaxes.objects.create(
                tax=taxation,product=created_product
            )
            
        if (data["ipf_provider"]["is_financed"]).lower()=="yes":
            try:
                payer=IBSPayer.objects.get(id=data["ipf_provider"]["ipf_id"])
            except:
                return Response({
                    "status":False,
                    "error":"payer with the id does not exist"
                },status=400)
            try:
                instalment=InstalmentPlan.objects.get(id=data["ipf_provider"]["instalment_plan_id"])
            except:
                 return Response({
                    "status":False,
                    "error":"payer with the id does not exist"
                },status=400)


            ipf=ProductIPFDetail.objects.update_or_create(
                payer=payer,product=created_product,instalment_plan=instalment)
            
            for b in data["provider_info"]["providers_id"]:
                try:
                    provider_hospital=Provider.objects.get(id=b["provider_id"])
                    product_provider=ProductProvider.objects.create(
                        provider=provider_hospital,product=created_product)
                except:
                    pass
            for h in data["provider_info"]["specialist_id"]:
                try:
                    specialist_wetu=Specialist.objects.get(id=h["specialist_id"])
                    product_provider=ProductSpecialist.objects.create(
                        specialist=specialist_wetu,product=created_product)
                except:
                    pass
        for m in data['section']:
            for x in m['plan_data']:

                for n in x['member_details']:
                
                    resp_data.append({
                    "cover_limit":x['cover_limit'],
                    "age":m['age'],
                    "cover_lebal":x['cover_lebal'],
                    "depedant":n['depedant_type'],
                    "member_representation":n['member_representation'],
                    "amount":n['amount']
                    })
                    benefit=BulkPlanBenefit.objects.create(
                    plan_name=data["plan_name"],
                    cover_limit=x["cover_limit"],
                    cover_lebal=x["cover_lebal"],
                    depedant_type=n['depedant_type'],
                    member_representation=n['member_representation'],
                    gross_amount_payable=n['amount'],
                    product=created_product,
                    )
                    if (data["product_type"]).lower()=="healthcare":
                        try:
                            age=AgeSetup.objects.get(id=m['age'])
                            benefit.age=age
                        except:
                            return Response({
                                    "status":False,
                                    "error":"age with the id does not exist"
                                },status=400)
                    benefit.save()
        response=ProductsListSerializer(created_product).data
        rep_data={
            "status":True,
            "message":"Products Created Successfully",
            "object":response
        }
        return Response(rep_data,status=200)


class EditSingleProductAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request,id):
        data=request.data
        query=Products.objects.get(id=id)
        serializer=ProductsListSerializer(query).data
        rep_data={
                "status":True,
                "message":"Single Product Fethed Successfully",
                "object":serializer
            }
        return Response(rep_data,status=200)
    def patch(self,request,id):
        data=request.data
        try:      
            obj=Products.objects.get(id=id)
            obj.product_name=data["product_name"]
            obj.product_description=data["product_description"]
            obj.number_of_policies=data["number_of_policies"]
            obj.distribution_channel=data["distribution_channel"]
            obj.gross_premium=data["gross_premium"]
            obj.product_image_url=data["product_image_url"]
            obj.maximum_children=data["maximum_children"]
            obj.maximum_spouses=data["maximum_spouses"]
            obj.stamp_duty=data["stamp_duty"]
            obj.commission=data["commission"]
            obj.save()
            serializer=ProductsListSerializer(obj).data
            rep_data={
                    "status":True,
                    "message":"Product Edited Successfully",
                    "object":serializer
                }
            return Response(rep_data,status=200)
        except:
                rep_data={
                    "status":False,
                    "message":"Product Does not exist",
                   
                        }
                return Response(rep_data,status=400)
    def delete(self,request,id):
        data=request.data
        obj=Products.objects.get(id=id)
        obj.delete()
        rep_data={
                    "status":True,
                    "message":"product Deleted Successfully",
                   
                        }
        return Response(rep_data,status=200)



class CreateNewPolicyClassAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request):
        data=request.data
        query=ProductPolicyClass.objects.all()
        serializer=ProductPolicyClassListSerializer(query,many=True).data
        rep_data={
                "status":True,
                "message":"Products policy classes Fethed Successfully",
                "object":serializer
            }
        return Response(rep_data,status=200)
    def post(self,request):
        data = request.data
        print(data)
        product_number=random.randint(10000,10000000)
        created=ProductPolicyClass.objects.create(
                policy_name=data["policy_name"],
                policy_description=data["policy_description"],
                productpolicy_number=product_number  
            )
 
        response=ProductPolicyClassListSerializer(created).data
        rep_data={
            "status":True,
            "message":"Products policy classes Fethed Successfully",
            "object":response
        }
        return Response(rep_data,status=200)

class CreateNewPolicyTypeClassAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request):
        data=request.data
        query=ProductPolicyType.objects.all()
        serializer=ProductPolicyClasstypeListSerializer(query,many=True).data
        rep_data={
                "status":True,
                "message":"Products policy type Fethed Successfully",
                "object":serializer
            }
        return Response(rep_data,status=200)
    def post(self,request):
        data = request.data
        print(data)
        product_number=random.randint(10000,10000000)
        try:
            policy=ProductPolicyClass.objects.get(id=data["policy_class"])
        except:
            return Response({
                "status":False,
                "error":"the policy class with the id does not exist"
            })
        created=ProductPolicyType.objects.create(
                policy_type_name=data["policy_type_name"],
                policy_type_description=data["policy_type_description"],
                policy_type_number=product_number,
                policy_class=policy
            )
 
        response=ProductPolicyClasstypeListSerializer(created).data
        rep_data={
            "status":True,
            "message":"Products policy types Fethed Successfully",
            "object":response
        }
        return Response(rep_data,status=200)
class EditSingleProductPolicyAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request,id):
        data=request.data
        query=ProductPolicyClass.objects.get(id=id)
        serializer=ProductPolicyClassListSerializer(query).data
        rep_data={
                "status":True,
                "message":"Single Product policy class Fethed Successfully",
                "object":serializer
            }
        return Response(rep_data,status=200)
    def patch(self,request,id):
        data=request.data
        try:       
            obj=ProductPolicyClass.objects.get(id=id)
            obj.policy_name=data["policy_name"]
            obj.policy_description=data["policy_description"]
            obj.save()
            serializer=ProductPolicyClassListSerializer(obj).data
            rep_data={
                    "status":True,
                    "message":"Product policy class Edited Successfully",
                    "object":serializer
                }
            return Response(rep_data,status=200)
        except:
                rep_data={
                    "status":False,
                    "message":"Product policy Does not exist",
                   
                        }
                return Response(rep_data,status=400)
    def delete(self,request,id):
        data=request.data
        obj=ProductPolicyClass.objects.get(id=id)
        obj.delete()
        rep_data={
                    "status":True,
                    "message":"product Policy Deleted Successfully",
                   
                        }
        return Response(rep_data,status=200) 
class EditSingleProductPolicyTypeAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request,id):
        data=request.data
        query=ProductPolicyType.objects.get(id=id)
        serializer=ProductPolicyClasstypeListSerializer(query).data
        rep_data={
                "status":True,
                "message":"Single Product policy class Fethed Successfully",
                "object":serializer
            }
        return Response(rep_data,status=200)
    def patch(self,request,id):
        data=request.data
        try:       
            obj=ProductPolicyType.objects.get(id=id)
            obj.policy_type_name=data["policy_type_name"]
            obj.policy_type_description=data["policy_type_description"]
            obj.save()
            serializer=ProductPolicyClasstypeListSerializer(obj).data
            rep_data={
                    "status":True,
                    "message":"Product policy type Edited Successfully",
                    "object":serializer
                }
            return Response(rep_data,status=200)
        except:
                rep_data={
                    "status":False,
                    "message":"Product policy type Does not exist",
                   
                        }
                return Response(rep_data,status=400)
    def delete(self,request,id):
        data=request.data
        obj=ProductPolicyType.objects.get(id=id)
        obj.delete()
        rep_data={
                    "status":True,
                    "message":"product Policy type Deleted Successfully",
                   
                        }
        return Response(rep_data,status=200) 



class ProvidersSampleUploadExcelView(APIView):
    permission_classes=[AllowAny]          
    def get(self,request):
        keys=['Provider Name','Region','Physical Address','Phone Number','Contact Other','Email Address']
        title="Providers Sample Format for Upload"
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename='+"providers-sample-excel"+'.xls'
        style0 = xlwt.easyxf('font: name Candara, color-index black, bold on;align: horiz centre')
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Report')
        ws.write_merge(0, 0, 0, len(keys),title.upper(), style0)
        style1 = xlwt.easyxf('font: name Candara, color-index black, bold on')   
        style2 = xlwt.easyxf('font: name Candara, color-index black, bold off')   
        for col_num in range(len(keys)):
            ws.write(1, col_num, keys[col_num], style1)
        wb.save(response)
        print("fininshed")
        return response



class SpecialistSampleUploadExcelView(APIView):
    permission_classes=[AllowAny]          
    def get(self,request):
        keys=['Specialist Name','Specialty','Hospital','Region','Specialist location','Specialist Contact']
        title="Specialist Sample Format for Upload"
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename='+"specialists-sample-excel"+'.xls'
        style0 = xlwt.easyxf('font: name Candara, color-index black, bold on;align: horiz centre')
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Report')
        ws.write_merge(0, 0, 0, len(keys),title.upper(), style0)
        style1 = xlwt.easyxf('font: name Candara, color-index black, bold on')   
        style2 = xlwt.easyxf('font: name Candara, color-index black, bold off')   
        for col_num in range(len(keys)):
            ws.write(1, col_num, keys[col_num], style1)
        wb.save(response)
        print("fininshed")
        return response


class UploadSpecialistView(APIView):
        parser_classes = (MultiPartParser,JSONParser)
        permission_classes = [AllowAny]
        def post(self,request): 
                data = request.data
                file=request.FILES['excel'].read()
                base64_encoded = base64.b64encode(file).decode('UTF-8')
                print(base64_encoded)
                
               
                with open(default_storage.path(data['filename']), 'wb') as f:
                        
                        f.write(base64.b64decode(str(base64_encoded).replace('data:application/vnd.ms-excel;base64,','')))
        
                file_path = os.path.join('media', data['filename'])
                print(data['filename'])
                files = {open(file_path, 'rb')}
        
                wb = open_workbook(default_storage.path(data['filename']))
                print(wb)
                
                worksheet = wb.sheets()[0]
                
                print(worksheet)
                excel_data = list()
                
                for row in range(2, worksheet.nrows):
                    e_prefix=random.randint(10000,10000000)
                    specialist_name =worksheet.cell_value(row, 0)
                    
                    specialty=worksheet.cell_value(row, 1)
                    provider=worksheet.cell_value(row, 2)
                    region=worksheet.cell_value(row, 3)
                    specialist_location=worksheet.cell_value(row, 4)
                    specialist_contact=worksheet.cell_value(row, 5)
                    hospital,created=Provider.objects.update_or_create(
                        name=provider,email=str(e_prefix)+"@gmail.com"
                    )
                    created_object=Specialist.objects.update_or_create(
                        name=specialist_name,
                        specialty=specialty,
                        region=region,
                        mobile_number=specialist_contact,
                        specialist_location=specialist_location,
                        provider=hospital

                    )
                object=Specialist.objects.all()
                ser=SpecialistListSerializer(object,many=True).data
                resp={
                    "status":True,
                    "message":"upload was successfull",
                    "specialists":ser
                        }
                return Response(resp,status=200)
                   





class UploadProvidersView(APIView):
        parser_classes = (MultiPartParser,JSONParser)
        permission_classes = [AllowAny]
        def post(self,request): 
                data = request.data
                file=request.FILES['excel'].read()
                base64_encoded = base64.b64encode(file).decode('UTF-8')
                print(base64_encoded)
                
               
                with open(default_storage.path(data['filename']), 'wb') as f:
                        
                        f.write(base64.b64decode(str(base64_encoded).replace('data:application/vnd.ms-excel;base64,','')))
        
                file_path = os.path.join('media', data['filename'])
                print(data['filename'])
                files = {open(file_path, 'rb')}
        
                wb = open_workbook(default_storage.path(data['filename']))
                print(wb)
                
                worksheet = wb.sheets()[0]
                
                print(worksheet)
                excel_data = list()
                serv_type=[]
                
                for row in range(2, worksheet.nrows):
                    provider_name =worksheet.cell_value(row, 0)
                    
                    region=worksheet.cell_value(row, 1)
                    physical_address=worksheet.cell_value(row, 2)
                    phone_contact=worksheet.cell_value(row, 3)
                    other_phone=worksheet.cell_value(row, 4)
                    email_contact=worksheet.cell_value(row, 5)
                    service_type1=worksheet.cell_value(row, 6)
                    service_type2=worksheet.cell_value(row, 7)
                    service_type3=worksheet.cell_value(row, 8)
                    service_type4=worksheet.cell_value(row, 9)
                    serv_type.append({
                         "service_type_1":service_type1,
                          "service_type_2":service_type2,
                           "service_type_3":service_type3,
                            "service_type_4":service_type4,
                    })
                   
                    created_object=Provider.objects.update_or_create(
                        name=provider_name,
                        other_phone=other_phone,
                        region=region,
                        mobile_number=phone_contact,
                        physical_address=physical_address,
                        email=email_contact,
                        service_type=serv_type
                    )
                object=Provider.objects.all()
                ser=ProviderListSerializer(object,many=True).data
                resp={
                    "status":True,
                    "message":"upload was successfull",
                    "providers":ser
                        }
                return Response(resp,status=200)
class KatabimaProductsAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request):
        data=request.data
        resp_data=[]
        for x in Products.objects.filter(is_active=True):
            print(x.id)
            produ=ProductsListSerializer(x).data
            ipf=ProductIPFDetail.objects.filter(product__id=x.id)
            ipf_serializer=IPFProviderListSerializer(ipf,many=True).data
            taxes=ProductTaxes.objects.filter(product__id=x.id)
            tax_ser=ProductTaxesListSerializer(taxes,many=True).data
            terms=ProductTerms.objects.filter(product__id=x.id)
            terms_ser=ProductTermsListSerializer(terms,many=True).data
            benefits=BulkPlanBenefit.objects.filter(product__id=x.id)
            benefits_ser=BulkPlanBenefitsListSerializer(benefits,many=True).data
            resp_data.append({
                 "status":True,
                 "product":produ,
                 "ipf_provider":ipf_serializer,
                 "taxes":tax_ser,
                 "terms":terms_ser,
                 "benefits":benefits_ser
            })
        return Response(resp_data,status=200)

class CreateProductCategoryAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request):
        data=request.data
      
        category=PolicyTypeCategory.objects.all()
        ser=CategoryListSerializer(category,many=True).data

        return Response({
            "status":True,
            "message":"categories was fetched successfully",
            "object":ser

        })
    def post(self,request):
        data=request.data
        try:
            types=ProductPolicyType.objects.get(id=data["policy_type_id"])
        except:
            return Response({
            "status":True,
            "message":"category was not found",

        },status=400)
        number=random.randint(10000,10000000)

        created=PolicyTypeCategory.objects.create(
                category_name=data["category_name"],
                category_description=data["category_description"],
                category_number=number
                )
        created.policy_type=types
        created.save()
        serializer=CategoryListSerializer(created).data
        return Response({
            "status":True,
            "message":"category created successfully",
            "data":serializer
        })
    

class EditProductCategoryAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]

    def get(self,request,id):
        data=request.data
        try:
            query=PolicyTypeCategory.objects.get(id=id)
            serializer=CategoryListSerializer(query).data
            rep_data={
                    "status":True,
                    "message":"Single Product policy category Fethed Successfully",
                    "object":serializer
                    }
            return Response(rep_data,status=200)

        except:
            rep_data={
                    "status":False,
                    "message":"Product policy category Does not exist",
                   
                        }
    
            return Response(rep_data,status=400)
    
    
    def patch(self,request,id):
        data=request.data
        try:       
            obj=PolicyTypeCategory.objects.get(id=id)
            obj.category_name=data["category_name"]
            obj.category_description=data["category_description"]
            obj.policy_type_number=data["policy_type_id"]
            obj.save()
            serializer=CategoryListSerializer(obj).data
            rep_data={
                    "status":True,
                    "message":"Product policy category Edited Successfully",
                    "object":serializer
                }
            return Response(rep_data,status=200)
        except:
                rep_data={
                    "status":False,
                    "message":"Product policy category Does not exist",
                   
                        }
                return Response(rep_data,status=400)
            
    def delete(self,request,id):
        data=request.data
        try:
            obj=PolicyTypeCategory.objects.get(id=id)
            obj.delete()
            rep_data={
                "status":True,
                "message":"Product policy category deleted successfully",
               
                    }
            return Response(rep_data,status=200)
        except:
            rep_data={
                "status":False,
                "message":"Product policy category Does not exist",
               
                    }
            return Response(rep_data,status=400)
        
        
class GetAllTypesInCategoryAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request,id):
        data=request.data
        try:
            class_product=ProductPolicyClass.objects.get(id=id)
            my_obj=ProductPolicyType.objects.filter(policy_class=class_product)
            my_data=ProductPolicyClasstypeListSerializer(my_obj,many=True).data
            rep_data={
                    "status":True,
                    "message":"Product policy types Fetched Successfully",
                    "object":my_data
                    }
            return Response(rep_data,status=200)

        except:
            rep_data={
                    "status":False,
                    "message":"Product policy class Does not exist",
                   
                        }
    
            return Response(rep_data,status=400)
        
class GetAllCategoryinTypesAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request,id):
        data=request.data
        try:
            class_type=ProductPolicyType.objects.get(id=id)
            my_obj=PolicyTypeCategory.objects.filter(policy_type=class_type)
            my_data=CategoryListSerializer(my_obj,many=True).data
            rep_data={
                    "status":True,
                    "message":"Product policy categories Fetched Successfully",
                    "object":my_data
                    }
            return Response(rep_data,status=200)

        except:
            rep_data={
                    "status":False,
                    "message":"Product policy category Does not exist",
                   
                        }
    
            return Response(rep_data,status=400)


class GetDashboardReportAPIView(APIView):
    parser_classes = (JSONParser, FormParser, MultiPartParser)
    permission_classes = [IsAuthenticated]

    def get(self, request):
            today = datetime.now().date()
            thirty_days_ago = today - timedelta(days=30)

            # Retrieve dashboard report data
            active_policies_count = Policies.objects.filter(status__icontains='active').count()
            renewals_count = Policies.objects.filter(status__icontains='renewal').count()
            product_counts = Products.objects.all().count()
            partner_counts = IBSPayer.objects.all().count()

            # Calculate account performance data
            gross_premiums = Policies.objects.filter(created__gte=thirty_days_ago).aggregate(Sum('premium'))['premium__sum'] or 0
            payments_received = MpesaPayment.objects.filter(created__gte=thirty_days_ago).aggregate(Sum('amount_received'))['amount_received__sum'] or 0
            commission = Policies.objects.filter(created__gte=thirty_days_ago).aggregate(Sum('commission'))['commission__sum'] or 0
            previous_month = thirty_days_ago - timedelta(days=30)
            previous_month_gross_premiums = Policies.objects.filter(created__range=[previous_month, thirty_days_ago]).aggregate(Sum('premium'))['premium__sum'] or 0
            trend = gross_premiums - previous_month_gross_premiums

            # Prepare the response data
            rep_data = {
                "status": True,
                "message": "Dashboard Report Fetched Successfully",
                "active_policies": active_policies_count,
                "renewals": renewals_count,
                "products": product_counts,
                "partners": partner_counts,
                "account_performance": {
                    "gross_premiums": gross_premiums,
                    "payments_received": payments_received,
                    "commission": commission,
                    "trend": trend
                }
            }

            return Response(rep_data, status=200)

       
