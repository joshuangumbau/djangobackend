from django.contrib import admin

from accounts.models import AccountModel


class AccountModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'other_name', 'phone', 'department', 'gender',
                    'user_type', 'is_active', 'is_superuser', 'is_staff', 'is_client', 'is_archive', 'created')
    list_filter = ('is_active', 'is_superuser', 'is_staff', 'is_client', 'is_archive')
    search_fields = ('email', 'first_name', 'last_name', 'phone')
    

admin.site.register(AccountModel, AccountModelAdmin)