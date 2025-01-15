from django.contrib import admin

from electronic_trade.models import Supplier


@admin.register(Supplier)
class SupplierModelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'supplier_type',
        'debt',
    )