
from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import serializers

from KYC.models import KYCTemplate, KYCTemplateSection, KYCTemplateSubSection, KycAnswersModel, SubSectionQuestions
from accounts.serializer import  OrganizationUserSerializer





class KYCTemplateListSerializer(serializers.ModelSerializer):
    organization=OrganizationUserSerializer()

    class Meta:
        model = KYCTemplate
        fields=('__all__')


class KYCTemplateSectionListSerializer(serializers.ModelSerializer):
    template=KYCTemplateListSerializer()

    class Meta:
        model = KYCTemplateSection
        fields=('__all__')


class KYCTemplatSubSectionListSerializer(serializers.ModelSerializer):
    section=KYCTemplateSectionListSerializer()

    class Meta:
        model = KYCTemplateSubSection
        fields=('__all__')

class SubSectionQuestionsListSerializer(serializers.ModelSerializer):
    # sub_section=KYCTemplatSubSectionListSerializer()

    class Meta:
        model =SubSectionQuestions
        fields=('__all__')

class SubSectionQuestionsAnswersListSerializer(serializers.ModelSerializer):
    question=SubSectionQuestionsListSerializer()
    client=OrganizationUserSerializer()

    class Meta:
        model =KycAnswersModel
        fields=('__all__')
class AnswersListSerializer(serializers.ModelSerializer):
    question=SubSectionQuestionsListSerializer()

    class Meta:
        model =KycAnswersModel
        fields=('product_id','question','id','answer','created')