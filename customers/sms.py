# works with both python 2 and 3
# from __future__ import print_function

# import africastalking
# username = "sandbox"
# api_key = "6df32144874ed725b7518aa6f47b1ff9be3a17594d40c1ec350e257630dd94eb"

# def send_messages():
#     # for row in sheet1.iter_rows(values_only=True):
#         name = "Mwangangi"
#         number ="+254724511073"
#         lesson = "database"
#         lesson_date = "Friday 12 March at 8.00 am "
#         # print(name,number)
#         message = f"hey {name}  Kindly note {lesson} lecture is scheduled on {lesson_date}"
#         try:
#             response = sms.send(message, [number])
#             print(response)
#         except Exception as e:
#             print(f"Uh oh we have a problem: {e}")

# send_messages()
# import requests

# url="https://quicksms.advantasms.com/api/services/sendsms/"
# class SMS:
#     def  __init__(self):
#         self.trials=0
#     def send_sms(self,phone,sms):
#         self.trials+=1
#         if self.trials > 5:
#             return False
#         data={
#             "apikey":"ecf03718097377d7cb11cbeba4089ad6",
#             "partnerID":"3343",
#             "message":sms,
#             "shortcode":"AARHOSPITAL",
#             "mobile":phone
#             }
#         resp=requests.post(url,json=data,timeout=50)
#         print(resp.text)
#         if resp.status_code!=200:
#             self.send_sms(phone,sms)
#         else:
#             return True
        


        #  SMS().send_sms("0724511073","Dear Cashier,\n {}\n\n Please call to enquire".format(text))
        
from __future__ import print_function
import africastalking

class SMS:
    def __init__(self):
        self.USERNAME = "sandbox"
        self.API_KEY = "b75df3eedb25092263b9aa98f8b4d9c8a4ce7fadc568bb19debcc98755b7cb1e"
        
        
        
        #INITIALIZE SDK
        africastalking.initialize(self.USERNAME, self.API_KEY)
        
        
        #GET THE SMS SERVICE
        self.sms = africastalking.SMS
        
    def send(self):
        
        #set the numbers you want to sent to in international format
        
        recipients = ["+254724511073", "+254711647510"]
        
        #set your message 
        
        message = "Hello there this is joshua"
        
        #sender id
        
        sender = "Joshuangumbau"
        
        try:
            #thats it hit send and we'll take care of the rest
            response = self.sms.send(message, recipients, sender)
            return response({
                'status': 'success',
                'message': 'Message sent successfully'              })
            
        except Exception as e:            
            return response({
                'status': 'error',
                'message': 'Message not sent'
              })            
if __name__ == "__main__":
    
    SMS = SMS()
        
    response = SMS.send()