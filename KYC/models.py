from django.db import models
import uuid
from django.contrib.postgres.fields import ArrayField, JSONField
from accounts.models import AccountModel
# from products.models import Products




class KYCTemplate(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    organization= models.ForeignKey(AccountModel,null=True,on_delete=models.CASCADE)
    kyc_name= models.CharField(max_length=200,default="DEFAULT TEMPLATE MODEL", null=True, blank=True)
    kyctemplate_number=models.CharField(max_length=200, unique=True)
    description= models.CharField(max_length=200,default="", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


class KYCTemplateSection(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    section_name= models.CharField(max_length=200,default="", null=True, blank=True)
    section_number=models.CharField(max_length=200, null=True, blank=True)
    template=models.ForeignKey(KYCTemplate,null=True,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

#SUSPEDEND USAGE OF THIS KYC TEMPLATE
class KYCTemplateSubSection(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    sub_section_name= models.CharField(max_length=200,default="", null=True, blank=True)
    subsection_number=models.CharField(max_length=200, null=True, blank=True)
    section=models.ForeignKey(KYCTemplateSection,null=True,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)



class SubSectionQuestions(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    question_name= models.CharField(max_length=200,default="", null=True, blank=True)
    field_type=models.CharField(max_length=200, null=True, blank=True)
    template=models.ForeignKey(KYCTemplate,null=True,on_delete=models.CASCADE)
    section=models.ForeignKey(KYCTemplateSection,null=True,on_delete=models.CASCADE)
    question_number=models.CharField(max_length=200, null=True, blank=True)
    defaults=JSONField(null=True, blank=True, default=dict)
    created = models.DateTimeField(auto_now_add=True)

class ProductKYC(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    question= models.ForeignKey(SubSectionQuestions,null=True,on_delete=models.CASCADE)
    # product=models.ForeignKey(Products,null=True,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)



class KycAnswersModel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    answer=models.CharField(max_length=200, null=True, blank=True)
    subsection_id=models.CharField(max_length=200, null=True, blank=True)
    question=models.ForeignKey(SubSectionQuestions,null=True,on_delete=models.CASCADE)
    product_id=models.CharField(max_length=200, null=True, blank=True)
    client=models.ForeignKey(AccountModel,null=True,on_delete=models.CASCADE)
    section=models.ForeignKey(KYCTemplateSection,null=True,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)