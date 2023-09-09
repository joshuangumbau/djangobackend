from django.contrib import admin

from customers.models import CustomerOrder, Policies

# from customers.models import Customer

class  CustomerAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'user', 'product', 'benefit', 'created')
    
# Register your models here.
admin.site.register(CustomerOrder, CustomerAdmin)
admin.site.register(Policies)
