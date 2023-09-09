import uuid
from django.db import models
from instalments.models import InstalmentPlan
from products.models import Products
from django.contrib.postgres.fields import JSONField

# from products.models import Products

# Create your models here.

class Taxes(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    tax_name= models.CharField(max_length=200, null=True,default="", blank=True)
    tax_code=models.CharField(max_length=200, null=True,default="", blank=True)
    tax_type=models.CharField(max_length=200, null=True,default="", blank=True)
    applicable_to=models.CharField(max_length=200, null=True,default="", blank=True)
    tax_value=models.FloatField(default=0, null=True)
    is_active=models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)



class Terms(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    description=models.TextField(max_length=200, null=True,default="", blank=True)
    terms_code=models.CharField(max_length=200, null=True,default="", blank=True)
    is_active=models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

class AgeSetup(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    age_to=models.IntegerField(default=0, null=True, blank=True)
    age_from=models.IntegerField(default=0, null=True, blank=True)
    age_code=models.CharField(max_length=200, null=True,default="", blank=True)
    created = models.DateTimeField(auto_now_add=True)

class ProductBenefits(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    cover_name= models.CharField(max_length=200, null=True,default="", blank=True)
    policy_type= models.CharField(max_length=200, null=True,default="", blank=True)
    cover_amount=models.FloatField( null=True, blank=True,default=100000)
    benefits_code=models.CharField(max_length=200, null=True,default="", blank=True)
    age=models.ForeignKey(AgeSetup,null=True,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,null=True,on_delete=models.CASCADE)
    instalment_plan=models.ForeignKey(InstalmentPlan,null=True,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)



class BenefitDetails(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    depedant_type= models.CharField(max_length=200, null=True,default="", blank=True)
    member_representation= models.CharField(max_length=200, null=True,default="", blank=True)
    gross_amount_payable=models.FloatField(default=0, null=True, blank=True)
    details_code=models.CharField(max_length=200, null=True,default="", blank=True)
    product_value= models.CharField(max_length=200, null=True,default="", blank=True)
    manufacture_year= models.CharField(max_length=200, null=True,default="", blank=True)
    benefit=models.ForeignKey(ProductBenefits,null=True,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
class ProductTaxes(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    tax= models.ForeignKey(Taxes,null=True,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,null=True,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

class ProductTerms(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    term= models.ForeignKey(Terms,null=True,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,null=True,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class InclusivePackage(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    rates_name=models.CharField(max_length=200, null=True,default="", blank=True)
    rate_cover_amount=models.FloatField(default=0, null=True, blank=True)
    limit_class=models.ForeignKey(ProductBenefits,null=True,on_delete=models.CASCADE)   
    created = models.DateTimeField(auto_now_add=True)



class PackageDetails(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    dependant_type=models.CharField(max_length=200, null=True,default="", blank=True)
    gross_payable=models.FloatField(default=0, null=True, blank=True)
    package_class=models.ForeignKey(InclusivePackage,null=True,on_delete=models.CASCADE)   
    created = models.DateTimeField(auto_now_add=True)

class BulkPlanBenefit(models.Model):
    #one
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    depedant_type= models.CharField(max_length=200, null=True,default="", blank=True)
    member_representation= models.CharField(max_length=200, null=True,default="", blank=True)
    gross_amount_payable=models.FloatField(default=0, null=True, blank=True)
    details_code=models.CharField(max_length=200, null=True,default="", blank=True)
    product_value= models.CharField(max_length=200, null=True,default="", blank=True)
    manufacture_year= models.CharField(max_length=200, null=True,default="", blank=True)
    cover_lebal= models.CharField(max_length=200, null=True,default="", blank=True)
    #two
    plan_name= models.CharField(max_length=200, null=True,default="", blank=True)
    policy_type= models.CharField(max_length=200, null=True,default="", blank=True)
    cover_limit=models.FloatField( null=True, blank=True,default=1)
    age=models.ForeignKey(AgeSetup,null=True,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,null=True,on_delete=models.CASCADE)
    instalment_plan=models.ForeignKey(InstalmentPlan,null=True,on_delete=models.CASCADE)
    status=models.CharField(max_length=200, null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)


class Provider(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    name= models.CharField(max_length=200, null=True,default="", blank=True)
    mobile_number=models.CharField(max_length=200,default="", null=True, blank=True)
    physical_address=models.CharField(max_length=200,default="", null=True, blank=True)
    other_phone=models.CharField(max_length=200,default="", null=True, blank=True)
    region=models.CharField(max_length=200,default="", null=True, blank=True)
    email= models.CharField(max_length=200,unique=True)
    status=models.CharField(max_length=200,default="NEW", null=True, blank=True)
    latitude = models.FloatField(blank=True,default=0, null=True)
    service_type=JSONField(null=True, blank=True, default={})
    longitude = models.FloatField(blank=True,default=0, null=True)
    created = models.DateTimeField(auto_now_add=True)

class Specialist(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    name= models.CharField(max_length=200, null=True,default="", blank=True)
    mobile_number=models.CharField(max_length=200,default="", null=True, blank=True)
    specialty=models.CharField(max_length=200,default="", null=True, blank=True)
    region=models.CharField(max_length=200,default="", null=True, blank=True)
    specialist_location=models.CharField(max_length=200,default="", null=True, blank=True)
    status=models.CharField(max_length=200,default="NEW", null=True, blank=True)
    provider=models.ForeignKey(Provider,null=True,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

class ProductSpecialist(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    specialist=models.ForeignKey(Specialist,null=True,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,null=True,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

class ProductProvider(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    provider=models.ForeignKey(Provider,null=True,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,null=True,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)