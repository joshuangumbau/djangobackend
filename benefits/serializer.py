from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import serializers
from decimal import Decimal
from benefits.models import AgeSetup, BenefitDetails, BulkPlanBenefit, InclusivePackage, PackageDetails, ProductBenefits, ProductTaxes, ProductTerms, Taxes, Terms,Provider, Specialist
from instalments.serializer import LinkedInstalmentPlanListSerializer
from products.serializer import ProductsListSerializer


class TaxesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Taxes
        fields=('__all__')


class TermsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Terms
        fields=('__all__')


class ListAgeSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeSetup
        fields=('__all__')


class ProductBenefitsListSerializer(serializers.ModelSerializer):
    product=ProductsListSerializer()
    age=ListAgeSetupSerializer()
    class Meta:
        model = ProductBenefits
        fields=('__all__')
class policyProductBenefitsListSerializer(serializers.ModelSerializer):
    # product=ProductsListSerializer()
    # age=ListAgeSetupSerializer()
    class Meta:
        model = ProductBenefits
        fields=('__all__')


class BenefitsBenefitsListSerializer(serializers.ModelSerializer):
    benefit=ProductBenefitsListSerializer()
    class Meta:
        model = BenefitDetails
        fields=('__all__')

class SingleBenefitsDetailsListSerializer(serializers.ModelSerializer):
     
    monthly_instalment_fee=SerializerMethodField()
    initial_payment_fee=SerializerMethodField()
          
    class Meta:
        model = BenefitDetails
        fields=("depedant_type","member_representation","gross_amount_payable","details_code","id","monthly_instalment_fee","initial_payment_fee",)
    def get_monthly_instalment_fee(self, obj):
        try:
            plan=obj.benefit.instalment_plan.no_of_instalments
            monthly=int(obj.gross_amount_payable)/int(plan)
            return round(monthly, 2)
        except:
            return "Instalment plan is Null"
    def get_initial_payment_fee(self, obj):
        try:
            plan=obj.benefit.instalment_plan.no_of_instalments
            first=obj.benefit.instalment_plan.no_of_first_months
            monthly=(int(obj.gross_amount_payable)/int(plan))*int(first)
            return round(monthly, 2)
        except:
            return "Instalment plan is Null"



class SingleProductBenefitsListSerializer(serializers.ModelSerializer):
    instalment_plan=LinkedInstalmentPlanListSerializer()
    class Meta:
        model = ProductBenefits
        fields=('__all__')




class InclusivePackageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = InclusivePackage
        fields=('__all__')

class PackageDetailsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageDetails
        fields=('__all__')
class ProductTaxesListSerializer(serializers.ModelSerializer):
    tax=TaxesListSerializer()
    class Meta:
        model = ProductTaxes
        fields=('__all__')

class ProductTermsListSerializer(serializers.ModelSerializer):
    term=TermsListSerializer()
    class Meta:
        model = ProductTerms
        fields=('__all__')

class ProductTaxesListSerializer(serializers.ModelSerializer):
    tax=TaxesListSerializer()
    class Meta:
        model = ProductTaxes
        fields=('__all__')

class BulkPlanBenefitsListSerializer(serializers.ModelSerializer):
    age=ListAgeSetupSerializer()
    class Meta:
        model = BulkPlanBenefit
        fields=('__all__')
        


class ProviderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Provider
        fields=('__all__')


class SpecialistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Specialist
        fields=('__all__')
        
