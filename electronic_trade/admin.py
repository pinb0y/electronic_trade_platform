from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from electronic_trade.models import Supplier, Contact, Product


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'model',
        'release_date',
    )


class ContactsCityFilter(admin.SimpleListFilter):
    title = 'Город'
    parameter_name = 'city'

    def lookups(self, request, model_admin):
        cities = Contact.objects.values("city").distinct()
        return [(city['city'], city['city']) for city in cities]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(contacts__city=self.value())
        return queryset


class ContactsInline(admin.StackedInline):
    model = Contact
    fields = (
        'email',
        'country',
        'city',
        'street',
        'street_number',
    )
    extra = 1


@admin.action(description="Обнулить задолженность")
def clear_debt(self, request, queryset):
    queryset.update(debt=0)


@admin.register(Supplier)
class SupplierModelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'supplier_type',
        'supplier_change',
        'debt',
    )

    @admin.display(
        description='Поставщик родитель'
    )
    def supplier_change(self, obj: Supplier):
        if obj.supplier is None:
            return '-'
        edit_url = reverse(
            f"admin:{obj._meta.app_label}_{obj._meta.model_name}_change",
            args=(obj.supplier.pk,),
        )
        return mark_safe(
            f'<a class="grp-button" href="{edit_url}" target="blank">{obj.supplier.name}</a>'
        )

    list_filter = (ContactsCityFilter,)
    actions = (clear_debt,)
    inlines = (ContactsInline,)
