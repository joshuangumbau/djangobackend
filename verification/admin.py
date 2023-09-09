from django.contrib import admin
from .models import phoneModel

# Register your models here.
# class phoneModelAdmin(admin.ModelAdmin):
#     list_display = ('mobile', 'isVerified', 'counter')

admin.site.register(phoneModel)
