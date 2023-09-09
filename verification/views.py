from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
import pyotp
from rest_framework.response import Response
from rest_framework.views import APIView
from customers.sms import SMS

from verification.serializer import OtpListSerializer
from verification.utilis import convert_phone
from .models import phoneModel
import base64
import africastalking


class generateKey:
    @staticmethod
    def returnValue(phone):
        return str(phone) + str(datetime.date(datetime.now())) + "Some Random Secret Key"


class getPhoneNumberRegistered(APIView):
    @staticmethod

    def get(request):
        username = "katabima"    
        api_key = "eb5095975a73fdce7f8be9c8b29d4b750c53be89e75e376589f0eb9d50c8deb5"    
        africastalking.initialize(username, api_key)
        sms = africastalking.SMS
        try:
            phone=request.query_params.get("phone")
            
            Mobile = phoneModel.objects.get(Mobile=phone)  
        except ObjectDoesNotExist:
            phoneModel.objects.create(
                Mobile=phone,
            )
            Mobile = phoneModel.objects.get(Mobile=phone)
        Mobile.counter += 1 
        Mobile.save()
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())
        OTP = pyotp.HOTP(key)
        print(OTP.at(Mobile.counter))
        code=OTP.at(Mobile.counter)
        sms_number=convert_phone(phone)
        print(sms_number)
        message="Your One Time Password is "+str(code)
        response = sms.send(message, [sms_number])
        print(response)
       
        resp_data=({"status":True,
            "message":"otp was generated successfully",
            "OTPgenerated otp code": OTP.at(Mobile.counter)}),
            
   
        return Response(resp_data, status=200)
       
    @staticmethod
    def post(request):
        data=request.data
        try:
            phone=data["phone"]
        except:
            return Response({
                "status":False,
                "error":"Phone number is invalid"
            })
        try:
            otp=data["otp"]
        except:
            return Response({
                "status":False,
                "error":"There is no otp in the body provided"
            })
        try:
            Mobile = phoneModel.objects.get(Mobile=phone)
        except ObjectDoesNotExist:
            return Response("User does not exist", status=404)  

        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode()) 
        OTP = pyotp.HOTP(key) 
        if OTP.verify(otp, Mobile.counter):
            Mobile.isVerified = True
            Mobile.save()
            rep_data=OtpListSerializer(Mobile).data
            res=({
                "status":True,
                "message":"otp verification was successfull",
                "object":rep_data
            })
            return Response(res, status=200)
        error_resp=({
            "status":False,
            "error":"The provided otp is wrong"
        })
        return Response(error_resp, status=400)


# Time after which OTP will expire
# EXPIRY_TIME = 50 # seconds

# class getPhoneNumberRegistered_TimeBased(APIView):
#     # Get to Create a call for OTP
#     @staticmethod
#     def get(request, phone):
#         try:
#             Mobile = phoneModel.objects.get(Mobile=phone)  # if Mobile already exists the take this else create New One
#         except ObjectDoesNotExist:
#             phoneModel.objects.create(
#                 Mobile=phone,
#             )
#             Mobile = phoneModel.objects.get(Mobile=phone)  # user Newly created Model
#         Mobile.save()  # Save the data
#         keygen = generateKey()
#         key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
#         OTP = pyotp.TOTP(key,interval = EXPIRY_TIME)  # TOTP Model for OTP is created
#         print(OTP.now())
#         # Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
#         resp_data=({
#             "status":True,
#             "message":"otp was generated successfully",
#             "OTPgenerated otp code": OTP.now(),
            
#         })
#         return Response(resp_data, status=200)  # Just for demonstration

    # This Method verifies the OTP
    # @staticmethod
    # def post(request, phone):
    #     try:
    #         Mobile = phoneModel.objects.get(Mobile=phone)
    #     except ObjectDoesNotExist:
    #         return Response("User does not exist", status=404)  # False Call

    #     keygen = generateKey()
    #     key = base64.b32encode(keygen.returnValue(phone).encode())  # Generating Key
    #     OTP = pyotp.TOTP(key,interval = EXPIRY_TIME)  # TOTP Model 
    #     if OTP.verify(request.data["otp"]):  # Verifying the OTP
    #         Mobile.isVerified = True
    #         Mobile.save()
    #         return Response("You are authorised", status=200)
    #     return Response("OTP is wrong/expired", status=400)

