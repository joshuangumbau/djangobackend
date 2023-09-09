from django.db import models
import uuid


class IBSPayer(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    payer_name= models.CharField(max_length=200, null=True,default="", blank=True)
    payer_address_code=models.CharField(max_length=200, null=True,default="", blank=True)
    payer_logo=models.TextField(max_length=200, null=True,default="", blank=True)
    physical_address=models.CharField(max_length=200, null=True,default="", blank=True)
    payer_code=models.CharField(max_length=200, null=True, blank=True)
    latitude=models.FloatField(default=0, blank=True)
    logitude=models.FloatField(default=0, blank=True)
    phone=models.CharField(max_length=200, null=True,default="", blank=True)
    email=models.EmailField(max_length=200, null=True, blank=True,unique=True)
    is_active=models.BooleanField(default=True)
    status=models.CharField(max_length=200, null=True,default="NEW", blank=True)
    created=models.DateTimeField(auto_now_add=True)


class InstalmentPlan(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    no_of_instalments= models.FloatField(null=True,default=0, blank=True)
    no_of_first_months=models.FloatField(null=True,default=0, blank=True)
    instament_code=models.FloatField(null=True,default=0, blank=True)
    payment_date=models.DateTimeField(null=True,default="", blank=True)
    payer=models.ForeignKey(IBSPayer,null=True,on_delete=models.CASCADE)
    pelnaty_type=models.CharField(max_length=200, null=True, blank=True)
    pelnaty_value=models.FloatField(max_length=200, null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)