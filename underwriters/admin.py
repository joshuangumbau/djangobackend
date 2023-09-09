from django.contrib import admin

from .models import Underwriters

from underwriters.models import Underwriters

class UnderwritersAdmin(admin.ModelAdmin):
    list_display = ('id', 'insurer_name', 'insurer_detail', 'insurer_detail_2', 'contact_person', 'desgnation',
                    'mobile_number', 'email_id', 'insurer_id', 'is_active', 'is_verified', 'status', 'profile_url',
                    'location_address', 'latitude', 'longitude', 'company_website_url', 'created')
    list_filter = ('is_active', 'is_verified')
    search_fields = ('insurer_name', 'email_id', 'insurer_id')
    

admin.site.register(Underwriters, UnderwritersAdmin)