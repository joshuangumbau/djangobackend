from django.db import models
import uuid
from accounts.models import AccountModel

from benefits.models import BenefitDetails, ProductBenefits
from instalments.models import IBSPayer
from products.models import Products


class CustomerOrder(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    user=models.ForeignKey(AccountModel,null=True,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,null=True,on_delete=models.CASCADE)
    benefit=models.ForeignKey(ProductBenefits,null=True,on_delete=models.CASCADE)
    benefit_details=models.ForeignKey(BenefitDetails,null=True,on_delete=models.CASCADE)
    order_number=models.CharField(max_length=200, null=True,default="", blank=True)
    order_amount=models.FloatField(null=True,default=0, blank=True)
    created=models.DateTimeField(auto_now_add=True)

class Policies(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    client=models.ForeignKey(AccountModel,null=True,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,null=True,on_delete=models.CASCADE)
    benefit=models.ForeignKey(ProductBenefits,null=True,on_delete=models.CASCADE)
    benefit_details=models.ForeignKey(BenefitDetails,null=True,on_delete=models.CASCADE)
    policy_number=models.CharField(max_length=200, null=True,unique=True, blank=True)
    premiums=models.CharField(max_length=200, null=True,default="", blank=True)
    business_type=models.CharField(max_length=200, null=True,default="New", blank=True)
    client_group=models.CharField(max_length=200, null=True,default="CORPORATE", blank=True)
    policy_type=models.CharField(max_length=200, null=True,default="", blank=True)
    document_no=models.CharField(max_length=200, null=True,default="", blank=True)
    approved_by=models.CharField(max_length=200, null=True,default="", blank=True)
    start_date= models.DateTimeField(blank=True, null=True)
    end_date= models.DateTimeField(blank=True, null=True)
    policy_amount=models.CharField(max_length=200, null=True,default="", blank=True)
    expiry=models.DateTimeField(auto_now_add=True)
    requested_by=models.CharField(max_length=200, null=True, blank=True)
    approved_by=models.CharField(max_length=200, null=True, blank=True)
    currency=models.CharField(max_length=200, null=True,default="KSH", blank=True)
    payer=models.ForeignKey(IBSPayer,null=True,on_delete=models.CASCADE)




    status=models.CharField(max_length=200, null=True,default="Pending", blank=True)
    created=models.DateTimeField(auto_now_add=True)
