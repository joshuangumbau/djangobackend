from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import serializers
from instalments.models import IBSPayer, InstalmentPlan
# from products.serializer import ProductsListSerializer

# from products.models import Products



class IBSPayerListSerializer(serializers.ModelSerializer):

    class Meta:
        model = IBSPayer
        fields=('__all__')


class InstalmentPlanListSerializer(serializers.ModelSerializer):
    payer=IBSPayerListSerializer()
    # product=ProductsListSerializer()

    class Meta:
        model = InstalmentPlan
        fields=('__all__')

class LinkedInstalmentPlanListSerializer(serializers.ModelSerializer):
    # payer=IBSPayerListSerializer()

    class Meta:
        model = InstalmentPlan
        fields=('__all__')