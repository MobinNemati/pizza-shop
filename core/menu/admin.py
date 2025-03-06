from django.contrib import admin
from .models import Category, Item, Order, OrderItem

class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'is_available', 'score', 'created_date']


admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)