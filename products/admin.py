from django.contrib import admin
from benefits.models import Provider, Specialist

from products.models import ProductPolicyClass, Products

from .models import PolicyTypeCategory, ProductIPFDetail, ProductPolicyType, Products

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_description', 
                     'product_image_url','underwriter', 'policy_class', 'is_active', 'is_verified', 'status',  'broker_commission',
                    'created')
    list_filter = ('is_active', 'is_verified', 'underwriter', 'policy_class')
    search_fields = ('product_name', 'product_description', 'product_number')
    
class ProductsPolicyClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'policy_name', 'productpolicy_number', 'policy_description', 'created')
    

class ProductsPolicyTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'policy_type_name','policy_type_number', 'policy_type_description', 'created')
    
admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductPolicyType, ProductsPolicyTypeAdmin)
admin.site.register(ProductPolicyClass, ProductsPolicyClassAdmin)
admin.site.register(Provider)
admin.site.register(Specialist)
admin.site.register(ProductIPFDetail)
admin.site.register(PolicyTypeCategory)

