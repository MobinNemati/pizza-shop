from django.contrib import admin
from .models import Contact, Employee, Reservation



class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'phone_number', 'created_date')
    list_filter = ('phone_number',)
    search_fields = ('name', 'message')





class ReservationAdmin(admin.ModelAdmin):
    list_display = ['customer', 'table_number', 'is_available', 'status']







admin.site.register(Contact, ContactAdmin)
admin.site.register(Employee)
admin.site.register(Reservation, ReservationAdmin)



