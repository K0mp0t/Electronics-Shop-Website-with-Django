from django.contrib import admin
from .models import *

class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0 

class OrdersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    search_fields = ['id']
    inlines = [ProductInOrderInline]
    
    class Meta:
        model = Order

admin.site.register(Order, OrdersAdmin)
