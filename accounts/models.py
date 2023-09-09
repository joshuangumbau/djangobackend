from django.db import models
import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from datetime import datetime
import django

from .managers import UserManager

__all__ = ['account']
class AccountModel(AbstractBaseUser,PermissionsMixin):
   
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100,blank=True,null=True)
    client_code = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    other_name = models.CharField(max_length=100,blank=True,null=True)
    phone = models.CharField(max_length=13,blank=True,null=True,unique=True)
    department = models.CharField(max_length=100,blank=True,null=True)
    gender = models.CharField(max_length=100,blank=True,null=True)
    user_type = models.CharField(max_length=100,blank=True,null=True) 
    role = models.CharField(max_length=100,blank=True,null=True)
    password= models.CharField(max_length=128, verbose_name='password')
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_client = models.BooleanField(default=False)
    is_archive = models.BooleanField(default = False)
    jwt_secret = models.UUIDField(default=uuid.uuid4)
    created=   models.DateTimeField(auto_now_add=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    class Meta:
        verbose_name = ('account')
        verbose_name_plural = ('accounts')


    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        return self.email

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.email

    def __unicode__(self):
        """
        Human redeable string representation of a user.
        """
        return self.email