
from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import serializers
from underwriters.models import Underwriters


class UnderwritersListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Underwriters
        fields=('__all__')