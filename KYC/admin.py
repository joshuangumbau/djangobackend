from django.contrib import admin

from KYC.models import KYCTemplate, KYCTemplateSection, KYCTemplateSubSection, KycAnswersModel, SubSectionQuestions

class KYCTemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'organization', 'kyc_name', 'kyctemplate_number', 'description', 'created')
    
class KYCTemplateSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'section_name', 'section_number', 'template', 'created')
    
class KYCTemplateSubSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_section_name', 'subsection_number', 'section', 'created')
    
class SubSectionQuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_name', 'field_type', 'template', 'section', 
                    'question_number', 'created')
    

class KycAnswersModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'answer', 'question', 'client', 'created')
    

admin.site.register(SubSectionQuestions, SubSectionQuestionsAdmin)
admin.site.register(KycAnswersModel, KycAnswersModelAdmin)
admin.site.register(KYCTemplateSubSection, KYCTemplateSubSectionAdmin)
admin.site.register(KYCTemplateSection, KYCTemplateSectionAdmin)
admin.site.register(KYCTemplate, KYCTemplateAdmin)
