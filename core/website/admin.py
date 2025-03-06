from django.contrib import admin
from .models import Contact, Employee



class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'phone_number', 'created_date')
    list_filter = ('phone_number',)
    search_fields = ('name', 'message')



admin.site.register(Contact, ContactAdmin)
admin.site.register(Employee)



