from django.contrib import admin
from .models import WaitList


class WaitListAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'user_type')
    search_fields = ['user_type']


admin.site.register(WaitList, WaitListAdmin)
# Register your models here.
