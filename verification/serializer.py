from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import serializers

from verification.models import phoneModel
# from underwriters.models import Underwriters


class OtpListSerializer(serializers.ModelSerializer):

    class Meta:
        model = phoneModel
        fields=('__all__')