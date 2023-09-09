from django.db import models
import uuid


class Underwriters(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    insurer_name= models.CharField(max_length=200, null=True,default="", blank=True)
    insurer_detail= models.CharField(max_length=200,default="", null=True, blank=True)
    insurer_detail_2= models.CharField(max_length=200,default="", null=True, blank=True)
    contact_person= models.CharField(max_length=200,default="", null=True, blank=True)
    desgnation=models.CharField(max_length=200,default="", null=True, blank=True)
    mobile_number=models.CharField(max_length=200,default="", null=True, blank=True)
    email_id= models.CharField(max_length=200,unique=True)
    insurer_id=models.CharField(max_length=200, null=True, blank=True)
    is_active=models.BooleanField(default=True)
    is_verified = models.BooleanField(default=True)
    status=models.CharField(max_length=200,default="NEW", null=True, blank=True)
    profile_url = models.TextField(blank=True, null=True)
    location_address = models.CharField(max_length=255, blank=True)
    latitude = models.FloatField(blank=True,default=0, null=True)
    longitude = models.FloatField(blank=True,default=0, null=True)
    company_website_url = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)