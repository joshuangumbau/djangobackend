from django.urls import path, include
from .views import getPhoneNumberRegistered


urlpatterns = [
    path('create-get-verify-otp/', getPhoneNumberRegistered.as_view(), name="OTP Gen"),
    # path("time_based/<phone>/", getPhoneNumberRegistered_TimeBased.as_view(), name="OTP Gen Time Based"),
]