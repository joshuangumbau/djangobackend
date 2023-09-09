import uuid
from django.contrib.postgres.fields import JSONField

from django.db import models

class MpesaPayment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    amount = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    receipt_code = models.CharField(max_length=100,null=True,blank=True,unique=True)
    date=models.DateTimeField(null=True,blank=True)
    reference = models.CharField(max_length=100,null=True,blank=True)
    email= models.CharField(max_length=100,null=True,blank=True)
    type= models.CharField(max_length=100,null=True,blank=True)
    charge_id = models.CharField(max_length=100,null=True,blank=True)
    callback_id = models.CharField(max_length=100,null=True,blank=True)
    channel = models.CharField(max_length=100,null=True,blank=True)
    status = models.CharField(max_length=100,null=True,blank=True)
    status_code=models.CharField(max_length=100,null=True,blank=True)
    phone_number = models.CharField(max_length=100,null=True,blank=True)
    is_utilized=models.BooleanField(default=False)
    json_response= JSONField(null=True, blank=True, default=[])    
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Mpesa Payment'
        verbose_name_plural = 'Mpesa Payments'
    def __str__(self):
        try:
            return self.receipt_code
        except:
            return ''















class PushedSTKs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    amount = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    channel = models.CharField(max_length=100,null=True,blank=True)
    reference = models.CharField(max_length=100,null=True,blank=True)
    source_id = models.CharField(max_length=100,null=True,blank=True)
    mechant_app_id= models.CharField(max_length=100,null=True,blank=True)
    uuid= models.CharField(max_length=100,null=True,blank=True)
    stk_id=models.IntegerField(unique=True)
    created = models.DateTimeField(auto_now_add=True)