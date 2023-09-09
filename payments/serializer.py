from rest_framework import serializers
from rest_framework.serializers import ModelSerializer,SerializerMethodField
import json

from payments.models import MpesaPayment



class MpesaSerialiser(serializers.ModelSerializer):
    
   
    class Meta:
        model = MpesaPayment
        fields = ('__all__')
            