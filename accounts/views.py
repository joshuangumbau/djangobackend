import random
from django.shortcuts import render
# from django_otp.oath import TOTP
# from django_otp.util import random_hex
# from unittest import mock
# import time
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from djang.totp_verification import TOTPVerification

# Create your views here.
import dataclasses
from datetime import datetime
from django.shortcuts import render
from accounts.serializer import  LoginSerializer, UserLoginSerializer
from rest_framework import permissions
from rest_framework.views import APIView

from .models import AccountModel
from django.shortcuts import get_object_or_404

from rest_framework import status, viewsets
from rest_framework.decorators import (api_view, parser_classes,
                                       permission_classes)
from rest_framework.parsers import JSONParser,MultiPartParser,FormParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_302_FOUND, HTTP_400_BAD_REQUEST


from django.core.mail import EmailMultiAlternatives

@api_view(['POST'])
@permission_classes((AllowAny,))
@parser_classes((JSONParser,FormParser,MultiPartParser ))
def login(request):
    data = request.data
    
    print(data)
    serializer = LoginSerializer(data=data, context={'request': request})
    if not serializer.is_valid():
        return Response({'error': 'blank username or password'}, status=401)
    user = get_object_or_404(AccountModel,email=serializer.validated_data['email'])
    if not user.check_password(serializer.validated_data['password']):
        return Response({'error': 'Incorrect username or password'}, status=401)
    serializer = UserLoginSerializer(user)
   
    data = serializer.data
   
    login_time=datetime.now()
   
    obj=AccountModel.objects.get(email=user.email)
   
    
    obj.last_login==login_time
    obj.save()
    return Response(data)

#authentication token

# class TOTPVerification:
#         def __init__(self, key=None, number_of_digits=6, token_validity_period=30):
#             self.key = key or TOTP.random_base32()
#             self.last_verified_counter = -1
#             self.verified = False
#             self.number_of_digits = number_of_digits
#             self.token_validity_period = token_validity_period

#         def totp_obj(self):
#             totp = TOTP(self.key, step=self.token_validity_period, digits=self.number_of_digits)
#             totp.time = time.time()
#             return totp

#         def generate_token(self):
#             totp = self.totp_obj()
#             token = str(totp.token()).zfill(self.number_of_digits)
#             return token

#         def verify_token(self, token, tolerance=0):
#             try:
#                 token = int(token)
#             except ValueError:
#                 self.verified = False
#             else:
#                 totp = self.totp_obj()
#                 if (totp.t() > self.last_verified_counter) and (totp.verify(token, tolerance=tolerance)):
#                     self.last_verified_counter = totp.t()
#                     self.verified = True
#                 else:
#                     self.verified = False
#             return self.verified
        

# @csrf_exempt
# def generate_token(request):
#     if request.method == 'POST':
#         phone = TOTPVerification()
#         token = phone.generate_token()
#         return JsonResponse({'token': token})
#     else:
#         return JsonResponse({'error': 'Invalid request method'})

# @csrf_exempt
# def verify_token(request):
#     if request.method == 'POST':
#         token = request.POST.get('token')
#         if token:
#             phone = TOTPVerification()
#             result = phone.verify_token(token)
#             return JsonResponse({'verified': result})
#         else:
#             return JsonResponse({'error': 'Token not provided'})
#     else:
#         return JsonResponse({'error': 'Invalid request method'})
    
    
    
class ResetPasswordAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[AllowAny]
    def post(self,request):
        data = request.data
        print(data)
        try:
                accountModel=AccountModel.objects.filter(is_archive=False).get(email=data['email'])
                if  accountModel != None:
                        
                        val="IBS"+str(random.randint(10000,10000000))
                        passwordreset=val
                        subject, from_email, to = 'Password Reset Details', 'thebhubinfor@gmail.com',data['email']
                        accountModel.set_password(passwordreset)
                        print(passwordreset)
                        accountModel.save()
                        text_content = ''
                        html_content = """
                        <h4>Hi  """ +accountModel.email+""" </h4>
                        <div style="margin-left:5px;font-size:12px">
                        You have successfully Reset your account for the IBS system <a href="https://ibs/bhub/#/login">https://ibs/bhub/#/login</a> <br>
                        Below are your Credentials.<br>
                        <b>Username</b>: """+accountModel.email+"""<br>
                        <b>Password</b>:"""+str(passwordreset)+"""
                        <br>
                        <br>
                        Please Login Using the Above Credentials,<br>
                        You can Opt to Reset Your preffered Password  on the Dashboard after Login.<br>
                        </div>

                        <div>
                        Regards,<br>
                        Bhub Support,<br>
                        
                        </div>
                        """
                        print("tunaanza")
                        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                        msg.attach_alternative(html_content, "text/html")
                        print("sending....")
                        # print("from":from)
                        msg.send()
                        return Response({"success":"Password Reset Successfull"},status=HTTP_200_OK)
                    
                return Response({"error":"Passwords does not match"},status=HTTP_400_BAD_REQUEST)
        except:
            return Response({"status":False,"error":"user with that email does not exist"})







# @api_view(['POST'])
# @permission_classes((AllowAny,))
# @parser_classes((JSONParser,FormParser,MultiPartParser ))
# def JoinChezaaAfrica(request):
            
#         try:
#             data = request.data
#             print(data)
#             client, created=AccountModel.objects.update_or_create(
#                 email=data['email'],
#                 defaults={
#                 'first_name':data['first_name'],
#                 'last_name':data['last_name'],
#                 'other_name':data['other_name'],
#                 'language':data['language'],
#                 'role':"user",
#                 'phone':data['phone'],
#                 'social_media':data['social_media'],
#                 'facebook':data['facebook'],
#                 'youtube':data['youtube'],
#                 'country':data['country']
#                }
#             )
#             client.is_client=True
#             client.save()
#             # email="mwangangimuvisi@gmail.com"
#             email="kennedyoloo010@gmail.com"
#             subject, from_email, to = 'Approve New Client Requested! --'+ data['first_name'], 'info.healthixsolutions@gmail.com',email
#             text_content = ''
#             html_content = """
#             <h4>Dear ken,</h4>
#             <div style="margin-left:5px;font-size:12px">
#             There is new client Requested to join Chezaa Africa.<br>
#             <h4>1:Approve Details</h4>
#             <b>First Name:</b> """+data['first_name']+"""<br>
#             <b>Last Name:</b> """+data['last_name']+"""<br>
#             <b>Surname Name:</b> """+data['other_name']+"""<br>
#             <b>Email:</b> """+data['email']+"""<br>
#             <b>Phone:</b> """+str(data['phone'])+"""<br>
#             <b>Country:</b> """+data['country']+"""<br>
#             <b>Social Media:</b> """+data['social_media']+"""<br>
#             <b>FaceBook:</b> """+data['facebook']+"""<br>
#             <b>Youtube:</b> """+data['youtube']+"""<br>
#             <b>language:</b> """+data['language']+"""<br>

#             </div>
#             <div><br>
#             Kind Regards,<br>
#             Software Engineer,<br>
#             Chezaa Africa,<br>
#             Tel:0724511073<br>
#             </div>
#             """
#             print("tunaanza")
           
#             msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
#             msg.attach_alternative(html_content, "text/html")
           
#             print("sending....")
          
            
#             msg.send()
#             return Response({"status":True,"success":"CREATED SUCCESSFULL"})
#         except:


#             return Response({"status":False,"error":"Email Already exist"})
# @api_view(['GET'])
# @permission_classes((AllowAny,))
# @parser_classes((JSONParser,FormParser,MultiPartParser ))
# def ChezaaAfricaUsers(request):
#      data=request.data
#      queryset=AccountModel.objects.filter(is_client=True)
#      ser=ChezaafricaUsersSerializer(queryset,many=True).data
#      return Response(ser)
# @api_view(['POST'])
# @permission_classes((AllowAny,))
# @parser_classes((JSONParser,FormParser,MultiPartParser ))
# def ChezaaAfricaApprove(request):
#             data=request.data
#             print(data)
#             val=random.randint(1000,1000000)
#             print(val)
#             approve=AccountModel.objects.get(email=data['email'])
#             approve.approval_status="YES"
#             approve.passcode=val
#             approve.save()
#             # email="mwangangimuvisi@gmail.com"
#             email="kennedyoloo010@gmail.com"
#             subject, from_email, to = 'Congratulations! You have been Approved to join Chezaa Africa --'+ approve.first_name, 'info.healthixsolutions@gmail.com',email
#             text_content = ''
#             html_content = """
#             <h4>Congratulations! """+approve.first_name+""",</h4>
#             <div style="margin-left:5px;font-size:12px">
#             Your request to Join Chezaa Africa has been Approved.<br>
#             <h4>1:Complete your profile on the link below</h4>
#             <b>Find below passcode which will be needed to authenticate your page in the nex step</b>
#             <b>It will be needed to Update Your Profile and Completion</b>
#             <b>if by any chance you Did not Get your Passcode reach out Us</b>
#             <b>Link:</b> """+"https://chezaaafrica.com/sign-contract/"+"""<br>
#             <b>Auth Passcode:</b> """+str(val)+"""<br>
#             <b>User Email:</b> """+data['email']+"""<br>
            

#             </div>
#             <div><br>
#             Kind Regards,<br>
#             ICT Support,<br>
#             Chezaa Africa,<br>
#             Tel:0724511073<br>
#             </div>
#             """
#             print("tunaanza")
           
#             msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
#             msg.attach_alternative(html_content, "text/html")
           
#             print("sending....")
          
            
#             msg.send()
    
#             return Response(status=200)


# @api_view(['POST'])
# @permission_classes((AllowAny,))
# @parser_classes((JSONParser,FormParser,MultiPartParser ))
# def ChezaaAfricaDecline(request):
#             data=request.data
#             print(data)
#             approve=AccountModel.objects.get(email=data['email'])
#             approve.approval_status="DECLINED"
#             approve.passcode='DECLINED'
#             approve.save()
#             # email="mwangangimuvisi@gmail.com"
#             email="kennedyoloo010@gmail.com"
#             subject, from_email, to = 'Unfortunately! we cannot proceed with you'+ approve.first_name, 'info.healthixsolutions@gmail.com',email
#             text_content = ''
#             html_content = """
#             <h4>We are sorry! """+approve.first_name+""",</h4>
#             <div style="margin-left:5px;font-size:12px">
#             Your request to Join Chezaa Africa was declined.<br>
#             <p4>1:We are happy for Your intrest to work with Chezaa Africa</p4><br>
#             <p4>2:Unfortunately we have opted not to continue with You.</p4><br>
#             <p4>3:We will consider working with you in future</p4><br>
            

#             </div>
#             <div><br>
#             Kind Regards,<br>
#             Software Engineer,<br>
#             Chezaa Africa,<br>
#             Tel:0724511073<br>
#             </div>
#             """
#             print("tunaanza")
           
#             msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
#             msg.attach_alternative(html_content, "text/html")
           
#             print("sending....")
          
            
#             msg.send()
    
#             return Response(status=200)
# @api_view(['POST'])
# @permission_classes((AllowAny,))
# @parser_classes((JSONParser,FormParser,MultiPartParser ))
# def ChezaaAfricaContract(request):
#             data=request.data
#             print(data)
#             res=AccountModel.objects.get(email=data['email'])
#             authcode=res.passcode
#             print(authcode)
#             try:
#                 if(data['password']!=data['confirm_password']):
                      
#                         return Response({"error":"Password Mismatch! Please check your password"},status=400)
                      
#                 if(int(authcode)==int(data['passcode'])):
#                     res.set_password(data['password'])
#                     res.save()
#                     res={
#                         "message":"Successfully update account",
#                         "email":data['email'],
#                         "password":data['password']
#                     }
#                     return Response(res)
#                 if(int(authcode) !=int(data['passcode'])):
                
#                     return Response({"error":"Invalid Authcode! Please use the correct one"},status=500)
#             except:
#                     try:
#                         res.first_name=data['first_name']
#                         res.last_name=data['last_name']
#                         res.address=data['address']
#                         res.role="user"
#                         res.country=data['phone_number']
#                         res.save()
#                         res={
#                             "message":"Successfully update account",
#                             "email":data['email'],
#                             "password":data['password']
#                                 }
#                         return Response(res)
#                     except:
#                         res.country=data['country']
#                         res.payment=data['payment']
#                         res.save()
#                         # email="mwangangimuvisi@gmail.com"
#                         email="kennedyoloo010@gmail.com"
#                         subject, from_email, to = 'Congratulations! Login to portal Now', 'info.healthixsolutions@gmail.com',email
#                         text_content = ''
#                         html_content = """
#                         <h4>Congratulations!</h4>
#                         <div style="margin-left:5px;font-size:12px">
#                         Your request to Join Chezaa Africa Fully Approved.<br>
#                         <h4>1:Click the Link below to access the portal</h4>
#                         <b>Link:</b> """+"https://chezaaafrica.com/portal/"+"""<br>
#                         <b>Username:</b>"""+data['email']+""" <br>
#                         <b>Password:</b>"""+data['password']+""" <br>

                        

#                         </div>
#                         <div><br>
#                         Kind Regards,<br>
#                         Software Engineer,<br>
#                         Chezaa Africa,<br>
#                         Tel:0724511073<br>
#                         </div>
#                         """
#                         print("tunaanza")
                    
#                         msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
#                         msg.attach_alternative(html_content, "text/html")
                    
#                         print("sending....")
                    
                        
#                         msg.send()
#                         res={
#                         "message":"Successfully update account",
#                         "email":data['email']
#                             }
#                         return Response(res)
