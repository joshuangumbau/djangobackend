# # import africastalking
# import africastalking
# # TODO: Initialize Africa's Talking

# africastalking.initialize(
#     username='tunza-app',
#     api_key=' f3c98dde56409dcdf7d668729e2ae5fd6ac6bc1869d0ca2c3c5f68c3fc8493fc'
# )

# sms = africastalking.SMS

# class send_sms():

#     def send(self):
         
#          send_sms().sending()
#     def sending(self):
#             # Set the numbers in international format
#             recipients = ["+254722123123"]
#             # Set your message
#             message = "Hey AT Ninja!";
#             # Set your shortCode or senderId
#             sender = "XXYYZZ"
#             try:
#                 response = self.sms.send(message, recipients, sender)
#                 print (response)
#                 # send_sms().sending()
            
#             except Exception as e:
#                 print (f'Houston, we have a problem: {e}')

import requests
# SECRET_KEY="put your django secret key here"
# AT_API_KEY="put  your africastalking api key here"
# AT_USER_NAME=sandbox
# AT_FROM_VALUE="put your africastalking from value here"
# import random
# from django.shortcuts import render

# # Create your views here.
# import dataclasses
# from datetime import datetime
# from django.shortcuts import render
# from rest_framework import permissions
# from rest_framework.views import APIView
# from django.shortcuts import get_object_or_404
# from rest_framework import status, viewsets
# from rest_framework.decorators import (api_view, parser_classes,
#                                        permission_classes)
# from rest_framework.parsers import JSONParser,MultiPartParser,FormParser
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.response import Response
# from rest_framework.decorators import api_view, renderer_classes
# from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer


# url = "https://api.sandbox.africastalking.com/version1/messaging"

# headers = {'ApiKey': '6df32144874ed725b7518aa6f47b1ff9be3a17594d40c1ec350e257630dd94eb', 
#            'Content-Type': 'application/x-www-form-urlencoded',
#            'Accept': 'application/json'}

# data = {'username': 'sandbox',
#         'from': '7991',
#         'message': "Africa test !",
#         'to': '+254724511073'}


# import json
# @api_view(['POST'])
# @permission_classes((AllowAny,))
# @parser_classes((JSONParser,FormParser,MultiPartParser ))
# def make_post_request(request):  
#     response = requests.post( url = url, headers = headers, data = data )
#     print(response.text)
#     resp=json.dumps(response.text)

#     return Response(json.loads(resp))



# works with both python 2 and 3
# from __future__ import print_function

# import africastalking

# class SMS:
#     # def __init__(self):
# 		# Set your app credentials
# 	    self.username = "YOUR_USERNAME"
#         self.api_key = "YOUR_API_KEY"

#         # Initialize the SDK
#         africastalking.initialize(self.username, self.api_key)

#         # Get the SMS service
#         self.sms = africastalking.SMS

#     def send(self):
#             # Set the numbers you want to send to in international format
#             recipients = ["+254713YYYZZZ", "+254733YYYZZZ"]

#             # Set your message
#             message = "I'm a lumberjack and it's ok, I sleep all night and I work all day";

#             # Set your shortCode or senderId
#             sender = "shortCode or senderId"
#             try:
# 				# Thats it, hit send and we'll take care of the rest.
#                 response = self.sms.send(message, recipients, sender)
#                 print (response)
#             except Exception as e:
#                 print ('Encountered an error while sending: %s' % str(e))

# if __name__ == '__main__':
#     SMS().send()



