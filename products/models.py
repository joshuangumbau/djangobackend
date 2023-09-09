from django.db import models
import uuid
from KYC.models import KYCTemplate
# from benefits.models import  Specialist
from instalments.models import IBSPayer, InstalmentPlan
# from benefits.models import Taxes

from underwriters.models import Underwriters
class ProductPolicyClass(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    policy_name= models.CharField(max_length=200, null=True,default="", blank=True)
    productpolicy_number=models.CharField(max_length=200, null=True, blank=True)
    policy_description= models.CharField(max_length=200, null=True,default="", blank=True)
    created=models.DateTimeField(auto_now_add=True)

class ProductPolicyType(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    policy_type_name= models.CharField(max_length=200, null=True,default="", blank=True)
    policy_class=models.ForeignKey(ProductPolicyClass,null=True,on_delete=models.CASCADE)
    policy_type_number=models.CharField(max_length=200, null=True, blank=True)
    policy_type_description= models.CharField(max_length=200, null=True,default="", blank=True)
    created=models.DateTimeField(auto_now_add=True)

class PolicyTypeCategory(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    category_name= models.CharField(max_length=200, null=True,default="", blank=True)
    policy_type=models.ForeignKey(ProductPolicyType,null=True,on_delete=models.CASCADE)
    category_number=models.CharField(max_length=200, null=True, blank=True)
    category_description= models.CharField(max_length=200, null=True,default="", blank=True)
    created=models.DateTimeField(auto_now_add=True)

class Products(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    product_name= models.CharField(max_length=200, null=True,default="", blank=True)
    distribution_channel= models.CharField(max_length=200,default="", null=True, blank=True)
    product_description= models.CharField(max_length=200,default="", null=True, blank=True)
    product_image_url=models.CharField(max_length=200,default="", null=True, blank=True)
    active_period= models.IntegerField(default=0,null=True)
    product_number=models.CharField(max_length=200, null=True, blank=True)
    underwriter=models.ForeignKey(Underwriters,null=True,on_delete=models.CASCADE)
    kyc=models.ForeignKey(KYCTemplate,null=True,on_delete=models.CASCADE)
    policy_class=models.ForeignKey(ProductPolicyClass,null=True,on_delete=models.CASCADE)
    policy_type=models.ForeignKey(ProductPolicyType,null=True,on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)
    is_verified = models.BooleanField(default=True)
    is_financed=models.CharField(max_length=200,default="NEW", null=True, blank=True)
    status=models.CharField(max_length=200,default="NEW", null=True, blank=True)
    broker_commission = models.FloatField(blank=True,default=0, null=True)
    created = models.DateTimeField(auto_now_add=True)





class ProductIPFDetail(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    payer=models.ForeignKey(IBSPayer,null=True,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,null=True,on_delete=models.CASCADE)
    instalment_plan=models.ForeignKey(InstalmentPlan,null=True,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)








# class Taxes(models.Model):
#     id = models.UUIDField(primary_key=True,default=uuid.uuid4)
#     tax_name= models.CharField(max_length=200, null=True,default="", blank=True)
#     percent_tax=models.FloatField(default=0)
#     is_active=models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)



# class Terms(models.Model):
#     id = models.UUIDField(primary_key=True,default=uuid.uuid4)
#     product=models.ForeignKey(Products,null=True,on_delete=models.CASCADE)
#     description=models.TextField(max_length=200, null=True,default="", blank=True)
#     is_active=models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)