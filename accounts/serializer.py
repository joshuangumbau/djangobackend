from curses import meta
from dataclasses import field, fields
from re import A
from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import serializers
from .models import AccountModel

from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.utils import jwt_payload_handler
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=50)
    password = serializers.CharField()



class UserSerializer(ModelSerializer):
	class Meta:
		model=AccountModel
		fields=('id','email','first_name','last_name','is_active','is_staff','role','phone')

class AccountSerializer(ModelSerializer):
	token = serializers.SerializerMethodField()
	
	class Meta:
		model=AccountModel
		fields=('__all__')
class OrganizationUserSerializer(ModelSerializer):
	
	class Meta:
		model=AccountModel
		fields=("id","first_name","last_name","phone","user_type","email")
		
		
class UserLoginSerializer(AccountSerializer):
    def get_token(self, obj):
        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token





