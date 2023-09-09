
from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import serializers
from benefits.models import Provider, Specialist
from instalments.serializer import IBSPayerListSerializer, LinkedInstalmentPlanListSerializer

from products.models import PolicyTypeCategory, ProductIPFDetail, ProductPolicyClass, ProductPolicyType, Products
from underwriters.serializer import UnderwritersListSerializer
# from products.models import Products
# from underwriters.models import Underwriters

class ProductPolicyClasstypeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductPolicyType
        fields=('__all__')
class ProductPolicyClassListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductPolicyClass
        fields=('__all__')

class ProductsListSerializer(serializers.ModelSerializer):
    policy_class=ProductPolicyClassListSerializer()
    policy_type=ProductPolicyClasstypeListSerializer()
    underwriter=UnderwritersListSerializer()

    class Meta:
        model = Products
        fields=('__all__')

class OrderProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields=("product_name","product_description","product_image_url","id","product_number")


class policyProductListSerializer(serializers.ModelSerializer):
    underwriter=UnderwritersListSerializer()

    class Meta:
        model = Products
        fields=("product_name","product_description","product_image_url","id","product_number","underwriter")
class ProviderListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields=('__all__')
class SpecialistListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Specialist
        fields=('__all__')

class IPFProviderListSerializer(serializers.ModelSerializer):
    payer=IBSPayerListSerializer()
    instalment_plan=LinkedInstalmentPlanListSerializer()

    class Meta:
        model = ProductIPFDetail
        fields=('__all__')

class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = PolicyTypeCategory
        fields=('__all__')