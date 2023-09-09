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
from KYC.models import ProductKYC, SubSectionQuestions
from benefits.models import AgeSetup, BenefitDetails, InclusivePackage, PackageDetails, ProductBenefits, ProductTaxes, ProductTerms, Taxes, Terms, Provider, Specialist
from benefits.serializer import BenefitsBenefitsListSerializer, InclusivePackageListSerializer, ListAgeSetupSerializer, PackageDetailsListSerializer, ProductBenefitsListSerializer, SingleBenefitsDetailsListSerializer, SingleProductBenefitsListSerializer, TaxesListSerializer, TermsListSerializer, ProviderSerializer,SpecialistSerializer

from instalments.models import InstalmentPlan
from instalments.serializer import LinkedInstalmentPlanListSerializer
from products.models import Products
from products.serializer import ProductsListSerializer
class CreateIBSTaxesAPIView(APIView):
    permission_classes=[IsAuthenticated]
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    def get(self,request):
        data=request.data
        query=Taxes.objects.all()
        serializer=TaxesListSerializer(query,many=True).data
        rep_data={
                "status":True,
                "message":"Taxes Fethed Successfully",
                "object":serializer
            }
        return Response(rep_data,status=200)
    def post(self,request):
        data = request.data
        print(data)
        tax_code=random.randint(10000,10000000)
        created=Taxes.objects.create(
                tax_name=data["tax_name"],
                tax_type=data["tax_type"],
                applicable_to=data["applicable_to"],
                tax_code=tax_code,
                tax_value=int(data["tax_value"])/100 if data["tax_type"] =="Percent" else data["tax_value"] 
            )
        response=TaxesListSerializer(created).data
        rep_data={
            "status":True,
            "message":"Taxes Created Successfully",
            "object":response
        }
        return Response(rep_data,status=200)

class EditNewIBSTaxAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request,id):
        data=request.data
        try:
            query=Taxes.objects.get(id=id)
            serializer=TaxesListSerializer(query).data
            rep_data={
                    "status":True,
                    "message":"Tax Fethed Successfully",
                    "object":serializer
                }
            return Response(rep_data,status=200)
        except:
            rep_data={
                    "status":False,
                 "error":"Tax Does not exist",    
                }
            return Response(rep_data)
    def patch(self,request,id):
        data = request.data
        print(data)
        try:
            obj=Taxes.objects.get(id=id)  
            obj.tax_name=data["tax_name"]
            obj.tax_type=data["tax_type"]
            
            obj.tax_value=int(data["tax_value"])/100 if data["tax_type"] =="Percent" else data["tax_value"]
            obj.save() 
            response=TaxesListSerializer(obj).data
            rep_data={
                "status":True,
                "message":"Tax Edited Successfully",
                "object":response
            }
            return Response(rep_data,status=200)
        except:
            rep_data={
                    "status":False,
                    "error":"Tax Does not exist",
                    
                }
            return Response(rep_data)
    def delete(self,request,id):
        data = request.data
        print(data)
        obj=Taxes.objects.get(id=id)
        obj.delete()
        rep_data={
                    "status":True,
                    "error":"Tax Deleted Successfully",
                    
                }
        return Response(rep_data)
    


class CreateProductTermsAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request):
        data=request.data
        query=Terms.objects.all()
        serializer=TermsListSerializer(query,many=True).data
        rep_data={
                "status":True,
                "message":"Terms Fethed Successfully",
                "object":serializer
            }
        return Response(rep_data,status=200)
    def post(self,request):
        data = request.data
        print(data)
        terms_code=random.randint(10000,10000000)
        created=Terms.objects.create(
                description=data["description"],
                terms_code=terms_code,
            )
        response=TermsListSerializer(created).data
        rep_data={
            "status":True,
            "message":"Terms Created Successfully",
            "object":response
        }
        return Response(rep_data,status=200)
    

class EditProductTermsAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request,id):
        data=request.data
        try:
            query=Terms.objects.get(id=id)
            serializer=TermsListSerializer(query).data
            rep_data={
                    "status":True,
                    "message":"Terms Fethed Successfully",
                    "object":serializer
                }
            return Response(rep_data,status=200)
        except:
            rep_data={
                    "status":False,
                    "error":"Term Does not exist",
                    
                }
            return Response(rep_data)

    def patch(self,request,id):
        data = request.data
        print(data)
        try:
            obj=Terms.objects.get(id=id)  
            obj.description=data["description"]          
            obj.save() 
            response=TermsListSerializer(obj).data
            rep_data={
                "status":True,
                "message":"Term Edited Successfully",
                "object":response
            }
            return Response(rep_data,status=200)
        except:
            rep_data={
                    "status":False,
                    "error":"Term Does not exist",
                    
                }
            return Response(rep_data)
    def delete(self,request,id):
        data = request.data
        print(data)
        obj=Terms.objects.get(id=id)
        obj.delete()
        rep_data={
                    "status":True,
                    "error":"Term Deleted Successfully",
                    
                }
        return Response(rep_data)
    
class CreateProductBenefitsAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request,id):
        data=request.data
        query=ProductBenefits.objects.all()
        serializer=ProductBenefitsListSerializer(query,many=True).data
        rep_data={
                "status":True,
                "message":"Product Benefits Fethed Successfully",
                "object":serializer
            }
        return Response(rep_data,status=200)
    def post(self,request,id):
        data = request.data
        print(data)
        try:
            age=AgeSetup.objects.get(id=data["age_id"])
        except:
            return Response({
                "status":False,
                "error":"Age specified does not exist check the Id you are Passing"
            })
        try:
            product=Products.objects.get(id=id)
        except:
            return Response({
                "status":False,
                "error":"Product specified does not exist check the Id you are Passing"
            })
        try:
            instalment_plan=InstalmentPlan.objects.get(id=data["instalment_plan_id"])
        except:
            return Response({
                "status":False,
                "error":"Plan specified does not exist check the Id you are Passing"
            })
        benefit_code=random.randint(10000,10000000)
        created=ProductBenefits.objects.create(
                cover_name=data["cover_name"],
                cover_amount=data["cover_amount"],
                policy_type=data["policy_type"],
                benefits_code=benefit_code
            )
        created.product=product
        created.age=age
        created.instalment_plan=instalment_plan
        created.save()
        response=ProductBenefitsListSerializer(created).data
        rep_data={
            "status":True,
            "message":"Benefits Created Successfully",
            "object":response
        }
        return Response(rep_data,status=200)

 
class CreateProductBenefitsDetailsAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request):
        data=request.data
        query=BenefitDetails.objects.all()
        serializer=BenefitsBenefitsListSerializer(query,many=True).data
        rep_data={
                "status":True,
                "message":"Product Benefits details Fethed Successfully",
                "object":serializer
            }
        return Response(rep_data,status=200)
    def post(self,request,id):
        data = request.data
        print(data)
        try:
             benefit=ProductBenefits.objects.get(id=id)
        except:
            return Response({
                "status":False,
                "error":"Productbenefit specified does not exist check the Id you are Passing"
            })
        benefitdetails_code=random.randint(10000,10000000)
        created=BenefitDetails.objects.create(
                depedant_type=data["depedant_type"],
                
                gross_amount_payable=data["gross_amount_payable"],
                details_code=benefitdetails_code
            )
        if  data["depedant_type"]=="Spouse":
            representation="M+1"
        if  data["depedant_type"]=="Child":
            representation="M+2"
        if  data["depedant_type"]=="Principal":
            representation="Principal"
        
        created.member_representation= representation
        created.benefit=benefit
        created.save()
        response=BenefitsBenefitsListSerializer(created).data
        rep_data={
            "status":True,
            "message":"productbenefits Created Successfully",
            "object":response
        }
        return Response(rep_data,status=200)
    
class EditBenefitClassAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request,id):
        data=request.data
        try:
            query=ProductBenefits.objects.get(id=id)
            serializer=SingleProductBenefitsListSerializer(query).data
            rep_data={
                    "status":True,
                    "message":"Productbenefit Fethed Successfully",
                    "object":serializer
                }
            return Response(rep_data,status=200)
        except:
            rep_data={
                    "status":False,
                 "error":"Product benefit Does not exist",    
                }
            return Response(rep_data)
    def patch(self,request,id):
        data = request.data
        print(data)
        try:
            obj=ProductBenefits.objects.get(id=id)  
            obj.cover_name=data["cover_name"]
            obj.cover_amount=data["cover_amount"]
            # obj.age_from=data["age_from"]
            # obj.age_to=data["age_to"]
            obj.save() 
            response=ProductBenefitsListSerializer(obj).data
            rep_data={
                "status":True,
                "message":"Product benefit class Edited Successfully",
                "object":response
            }
            return Response(rep_data,status=200)
        except:
            rep_data={
                    "status":False,
                    "error":"product benefit class Does not exist",
                    
                }
            return Response(rep_data)
    def delete(self,request,id):
        data = request.data
        print(data)
        obj=ProductBenefits.objects.get(id=id)
        obj.delete()
        rep_data={
                    "status":True,
                    "error":"product benefit Deleted Successfully",
                    
                }
        return Response(rep_data)
    
class EditBenefitDetailsAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request,id):
            data=request.data
      
            query=BenefitDetails.objects.get(id=id)
            serializer=SingleBenefitsDetailsListSerializer(query).data
            rep_data={
                    "status":True,
                    "message":"BenefitDetails Fethed Successfully",
                    "object":serializer
                }
            return Response(rep_data,status=200)
      
    def patch(self,request,id):
        data = request.data
        print(data)
        try:
            obj=BenefitDetails.objects.get(id=id)  
            obj.gross_amount_payable=data["gross_amount_payable"]
            obj.depedant_type=data["depedant_type"]
            if  data["depedant_type"]=="Spouse":
                representation="M+1"
            if  data["depedant_type"]=="Child":
                representation="M+2"
            if  data["depedant_type"]=="Principal":
                representation="Principal"
            obj.member_representation=representation
            obj.save() 
            response=BenefitsBenefitsListSerializer(obj).data
            rep_data={
                "status":True,
                "message":"Product benefit detail Edited Successfully",
                "object":response
            }
            return Response(rep_data,status=200)
        except:
            rep_data={
                    "status":False,
                    "error":"product benefit detail Does not exist",
                    
                }
            return Response(rep_data)
    def delete(self,request,id):
        data = request.data
        print(data)
        obj=BenefitDetails.objects.get(id=id)
        obj.delete()
        rep_data={
                    "status":True,
                    "error":"product benefit detail Deleted Successfully",
                    
                }
        return Response(rep_data)
    

    

        

@api_view(['GET'])
@permission_classes((AllowAny,))
@parser_classes((JSONParser,FormParser,MultiPartParser ))
def  GetBenefitDetailsAPIView(request):
        product=request.query_params.get('product_id')
        benefit_class=request.query_params.get('benefit_class_id')
        if product and benefit_class:
            try:
                prod=Products.objects.get(id=product)
                product_ser=ProductsListSerializer(prod).data
                try:

                 
                    
                    productbenefit=ProductBenefits.objects.get(id=benefit_class)
                    prod_ser=SingleProductBenefitsListSerializer(productbenefit).data
                    query=BenefitDetails.objects.filter(benefit=productbenefit)
                    benefitsser=SingleBenefitsDetailsListSerializer(query,many=True).data
                    other_plans=InclusivePackage.objects.filter(limit_class=productbenefit)
                    data_plans=InclusivePackageListSerializer(other_plans,many=True).data
                    return Response({
                        "status":True,
                        "product":product_ser,
                        "benefit_class":prod_ser,
                        "benefit_details":benefitsser,
                        "extra_packages":data_plans
                    })
                except:
                    return Response({
                        "status":False,
                        "error":"Product benefit class does not exist"
                    })
            except:
                return Response(
                    {"status":False,
                    "error":"The product with ID does not exist"}
                )



class LinkTaxToProductAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def post(self,request,id):
        data=request.data
        
        product=Products.objects.get(id=id)
        
        try:
            tax=Taxes.objects.get(id=data["tax_id"])
            created=ProductTaxes.objects.update_or_create(
                product=product,tax=tax
            )
            rep_data={
                    "status":True,
                    "message":"Tax Linked Successfully",
                }
            return Response(rep_data,status=200)
        except:
            rep_data={
                    "status":False,
                 "error":"Tax Does not exist",    
                }
            return Response(rep_data)
class LinkTermsToProductAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def post(self,request,id):
        data=request.data
        
        product=Products.objects.get(id=id)
        
        try:
            term=Terms.objects.get(id=data["terms_id"])
            created=ProductTerms.objects.update_or_create(
                product=product,term=term
            )
            rep_data={
                    "status":True,
                    "message":"Terms Linked Successfully",
                }
            return Response(rep_data,status=200)
        except:
            rep_data={
                    "status":False,
                 "error":"Terms Does not exist",    
                }
            return Response(rep_data)
        
class LinkKYCToProductAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def post(self,request,id):
        data=request.data
    
        product=Products.objects.get(id=id)
        
        try:
            quiz=SubSectionQuestions.objects.get(id=data["question_id"])
            created=ProductKYC.objects.update_or_create(
                product=product,question=quiz
            )
            rep_data={
                    "status":True,
                    "message":"kyc Linked Successfully",
                }
            return Response(rep_data,status=200)
        except:
            rep_data={
                    "status":False,
                 "error":"kyc Does not exist",    
                }
            return Response(rep_data)
        


class AgeRangeAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request):
        data=request.data
        obj=AgeSetup.objects.all()
        serializer=ListAgeSetupSerializer(obj,many=True).data
        return Response({
            "status":True,
            "message":"age range fetched succesfully",
            "data":serializer
        })


    def post(self,request):
        data=request.data
        age_code=random.randint(10000,10000000)
        if (data["age_from"]>=data["age_to"]):
                return Response({
                    "status":False,
                    "error":"age_to  cannot be smaller than age_from"
                })
        created=AgeSetup.objects.create(age_from=data["age_from"],age_to=data["age_to"],age_code=age_code)
        obj=ListAgeSetupSerializer(created).data
        return Response({
            "status":True,
            "message":"age range created succesfully",
            "data":obj
        })



class EditAgeRangeAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request,id):
        data=request.data
        try:
            obj=AgeSetup.objects.get(id=id)
            serializer=ListAgeSetupSerializer(obj).data
            return Response({
                "status":True,
                "message":"age range fetched succesfully",
                "data":serializer
            })
        except:
            return Response({
                "status":False,
                "error":"Group With  id does not  Exist",
            })



    def patch(self,request,id):
        data=request.data
        
        try:
            if (data["age_from"]>=data["age_to"]):
                return Response({
                    "status":False,
                    "error":"age_to  cannot be smaller  than or equal to age_from"
                })
           
            obj=AgeSetup.objects.get(id=id)
            obj.age_from=data["age_from"]
            obj.age_to=data["age_to"]
            obj.save()
            serializer=ListAgeSetupSerializer(obj).data
            return Response({
                "status":True,
                "message":"Age range edit succesfully",
                "data":serializer
            })
        except:
            return Response({
                "status":False,
                "error":"Group With  iddoes not  Exist",
            })
    def delete(self,request,id):
        data=request.data
        
        try:
            obj=AgeSetup.objects.get(id=id)
            obj.delete()
            return Response({
                "status":True,
                "message":"Age range deleted succesfully",
              
            })
        except:
            return Response({
                "status":False,
                "error":"Group With  iddoes not  Exist",
            })
        

class CreateOtherPackageAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def post(self,request):
        data=request.data
        try:
            package=ProductBenefits.objects.get(id=data["benefits_id"])
        except:
            return Response({
                "status":True,
                "message":"Benefits class  does not exist",
               
            })

      
        created=InclusivePackage.objects.create(
                rates_name=data["rates_name"],
                rate_cover_amount=data["rate_cover_amount"]
                )
        created.limit_class=package
        created.save()
        serializer=InclusivePackageListSerializer(created).data
        return Response({
            "status":True,
            "message":"package created successfully",
            "data":serializer
        })
       

class CreateOtherPackageDetailsAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def post(self,request):
        data=request.data
        try:
            package=InclusivePackage.objects.get(id=data["package_id"])
        except:
            return Response({
                "status":True,
                "message":"package does not exist",
               
            })

      
        created=PackageDetails.objects.create(
                dependant_type=data["dependant_type"],
                gross_payable=data["gross_payable"]
                )
        created.package_class=package
        created.save()
        serializer=PackageDetailsListSerializer(created).data
        return Response({
            "status":True,
            "message":"package_details created successfully",
            "data":serializer
        })
    



class CreateMotorProductBenefitsAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request,id):
        data=request.data
        query=ProductBenefits.objects.all()
        serializer=ProductBenefitsListSerializer(query,many=True).data
        rep_data={
                "status":True,
                "message":"Product Benefits Fethed Successfully",
                "object":serializer
            }
        return Response(rep_data,status=200)
    def post(self,request,id):
        data = request.data
        print(data)

        try:
            product=Products.objects.get(id=id)
        except:
            return Response({
                "status":False,
                "error":"Product specified does not exist check the Id you are Passing"
            })
        try:
            instalment_plan=InstalmentPlan.objects.get(id=data["instalment_plan_id"])
        except:
            return Response({
                "status":False,
                "error":"Plan specified does not exist check the Id you are Passing"
            })
        benefit_code=random.randint(10000,10000000)
        created=ProductBenefits.objects.create(
                policy_type=data["policy_type"],
                benefits_code=benefit_code
            )
        created.product=product
        try:
            created.cover_name=data["cover_name"]
        except:
            pass
        try:
            created.cover_amount=data["cover_amount"]
        except:
            pass
        created.instalment_plan=instalment_plan
        created.save()
        response=ProductBenefitsListSerializer(created).data
        rep_data={
            "status":True,
            "message":"Benefits Created Successfully",
            "object":response
        }
        return Response(rep_data,status=200)
    




class CreateMotorProductBenefitsDetailsAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request,id):
        data=request.data
        print(id)
        query=BenefitDetails.objects.all()
        serializer=BenefitsBenefitsListSerializer(query,many=True).data
        rep_data={
                "status":True,
                "message":"Product Benefits details Fethed Successfully",
                "object":serializer
            }
        return Response(rep_data,status=200)
    def post(self,request,id):
        data = request.data
        print(data)
        try:
             benefit=ProductBenefits.objects.get(id=id)
        except:
            return Response({
                "status":False,
                "error":"Productbenefit specified does not exist check the Id you are Passing"
            })
        benefitdetails_code=random.randint(10000,10000000)
        created=BenefitDetails.objects.create(
                product_value=data["product_value"],
                
                manufacture_year=data["manufacture_year"],
                details_code=benefitdetails_code
            )

        created.benefit=benefit
        created.save()
        response=BenefitsBenefitsListSerializer(created).data
        rep_data={
            "status":True,
            "message":"productbenefits Created Successfully",
            "object":response
        }
        return Response(rep_data,status=200)




# class CreateMotorProductBenefitAPIView(APIView):
#     parser_classes=(JSONParser,FormParser,MultiPartParser)
#     permission_classes=[AllowAny]
#     def post(self,request):
#         data=request.data
#         return Response(status=200)


class CreateNewProviderAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def  get(self, request):
        
 
        queryset = Provider.objects.all()
        serializer = ProviderSerializer(queryset, many=True)
        return Response({
            "status" : True,
            "message" : "Specialist List Fetched Successfully",
            "object" : serializer.data
        })
    

    def post(self,request):
        serializer = ProviderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class EditProviderDetailsAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def  get(self, request,id ):
        try:
        
    
            queryset = Provider.objects.get(id=id)
            serializer = ProviderSerializer(queryset).data
            return Response({
            "status" : True,
            "message" : "Provider Fetched Successfully",
            "object" : serializer
            })
        except:
            return Response({
            "status" : False,
            "error" : "Provider with Id does not exist",

        })
    def patch(self, request,id):
        data = request.data
        try:
        
    
            obj = Provider.objects.get(id=id)
            obj.name = data["name"]
            obj.email = data["email"]
            obj.mobile_number = data["mobile_number"]
            obj.physical_address = data["physical_address"]
            obj.other_phone = data["other_phone"]
            obj.region = data["region"]
            obj.latitude = data["latitude"]
            obj.longitude = data["longitude"]
            
            obj.save()
            
            serializer = ProviderSerializer(obj).data
            return Response({
                "status" : True,
                "message" : "Provider updated Successfully",
                "object" : serializer
            })
        except:
            return Response({
            "status" : False,
            "error" : "Provider with Id does not exist",

        })
         
         
         
    def delete(self, request,id):
        data = request.data
        try:
        
    
            obj = Provider.objects.get(id=id)
            obj.delete()
            # serializer = ProviderSerializer(obj).data
            return Response({
                "status" : True,
                "message" : "Provider deleted Successfully",
            })
        except:
         return Response({
            "status" : False,
            "error" : "Provider with Id does not exist",

        })
         
class CreateNewSpecialistAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self, request):
        specialists = Specialist.objects.all()
        serializer = SpecialistSerializer(specialists, many=True)
        return Response({
            "status" : True,
            "message" : "Specialist List Fetched Successfully",
            "object" : serializer.data
        })

    def post(self, request):
        serializer = SpecialistSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                "status" : True,
                "message" : "Specialist Created Successfully",
                "object" : serializer.data
            }, status=status.HTTP_201_CREATED)
        except serializer.ValidationError as e:
            return Response({
                "status" : False,
                "errors" : e.detail
            }, status=status.HTTP_400_BAD_REQUEST)


class EditSpecialistDetailsAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self, id):
        try:
            obj=Specialist.objects.get(id=id)
            serializer = SpecialistSerializer(obj,many=True).data
            return Response({
                "status" : True,
                "message" : "Specialist Fetched Successfully",
                "object" : serializer
            })
        except:
            return Response(
                {
                    "status":False,
                    "error":"specialist with the id does not exist"
                },status=400
            )

    def patch(self, request, id):
        data=request.data
        try:
            obj=Specialist.objects.get(id=id)
            obj.name=data["name"]
            obj.specialty=data["specialty"]
            obj.mobile_number=data["mobile_number"]
            obj.region=data["region"]
            obj.specialist_location=data["specialist_location"]
            obj.save()
            serializer = SpecialistSerializer(obj).data
            return Response({
                "status" : True,
                "message" : "Specialist was edited Successfully",
                "object" : serializer
            })
        except:
            return Response(
                {
                    "status":False,
                    "error":"specialist with the id does not exist"
                },status=400
            )
        
                
    def delete(self, request, id):
        data = request.data
        try:
            obj = Specialist.objects.get(id=id)
            obj.delete()
            return Response({
                "status" : True,
                "message" : "Specialist deleted Successfully",
            })
        except:
            return Response({
                "status" : False,
                "error" : "Specialist with Id does not exist",
            })
        



