from accounts.serializer import UserLoginSerializer
from benefits.serializer import ProductBenefitsListSerializer, SingleBenefitsDetailsListSerializer, policyProductBenefitsListSerializer
from customers.models import  CustomerOrder, Policies
from rest_framework import serializers

from products.serializer import OrderProductListSerializer, ProductsListSerializer, policyProductListSerializer

class CustomerListSerializer(serializers.ModelSerializer):
    user=UserLoginSerializer()
    product=OrderProductListSerializer()
    benefit_details=SingleBenefitsDetailsListSerializer()
    benefit=ProductBenefitsListSerializer()

    class Meta:
        model = CustomerOrder
        fields=('__all__')


class policyListSerializer(serializers.ModelSerializer):
    client=UserLoginSerializer()
    product=policyProductListSerializer()
    benefit_details=SingleBenefitsDetailsListSerializer()
    benefit=policyProductBenefitsListSerializer()

    class Meta:
        model = Policies
        fields=('__all__')