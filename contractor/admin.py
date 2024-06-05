from django.contrib import admin

from contractor import models
from contractor.models import Account, Contractor, Address



@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    """Админ-панель счетов"""
    list_display = ('id', 'inn', 'number_account')


@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    """Админ-панель поставщик"""

    list_display = ['name', 'address', 'bank_account', 'debt', 'provider', 'products_names']
    fields = ['name', 'address', 'bank_account', ('provider', 'levels'), 'products', 'debt']  # TODO сделать задолжность чтоб считалась и не исправ
    list_filter = ['address']   # TODO решить с городами, создать базу на русском, что вставить в фильтр?
    search_fields = ['name']
    actions = ['clear_arrears']

    @admin.action(description="Очищение задолженности")
    def clear_arrears(modeladmin, request, queryset):
        queryset.update(arrears=0)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    """Админ-панель счетов"""
    list_display = ['city',]

