from django.contrib import admin

from instalments.models import IBSPayer, InstalmentPlan

class IBSPayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'payer_name', 'payer_address_code', 'payer_logo', 'physical_address', 'payer_code', 'latitude'
                    ,'logitude', 'phone', 'phone', 'is_active', 'status', 'created')
    
class InstalmentPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'no_of_instalments', 'no_of_first_months', 'payment_date', 'payer'
                    ,'pelnaty_value' , 'created')
    
admin.site.register(IBSPayer, IBSPayerAdmin)
admin.site.register(InstalmentPlan, InstalmentPlanAdmin)