from django.contrib import admin

from benefits.models import AgeSetup, BenefitDetails, BulkPlanBenefit, InclusivePackage, PackageDetails, ProductBenefits, ProductTaxes, ProductTerms, Taxes, Terms

class BenefitDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'depedant_type', 'member_representation', 'gross_amount_payable', 'details_code', 'product_value', 'manufacture_year','benefit', 'created')
    list_filter = ('depedant_type', 'benefit')
    search_fields = ('depedant_type', 'member_representation')

class ProductBenefitsAdmin(admin.ModelAdmin):
    list_display = ('id', 'cover_name', 'policy_type', 'cover_amount', 'benefits_code', 'age', 'product', 'instalment_plan', 'created')
    
    
class ProductTaxesAdmin(admin.ModelAdmin):
    list_display = ('id', 'tax', 'created')
    
class ProductTermsAdmin(admin.ModelAdmin):
    list_display = ('id','term','product')
    
class TaxesAdmin(admin.ModelAdmin):
    list_display = ('id', 'tax_name', 'tax_code', 'tax_type', 'tax_value', 'created')
    
    
class TermsAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'created')
   
    
# admin.site.register(ProductBenefits, ProductBenefitsAdmin)
# admin.site.register(BenefitDetails, BenefitDetailsAdmin)
admin.site.register(ProductTaxes, ProductTaxesAdmin)
admin.site.register(Taxes, TaxesAdmin)
admin.site.register(Terms, TermsAdmin)
admin.site.register(ProductTerms, ProductTermsAdmin)
admin.site.register(InclusivePackage)
admin.site.register(PackageDetails)
admin.site.register(AgeSetup)
admin.site.register(BulkPlanBenefit)
