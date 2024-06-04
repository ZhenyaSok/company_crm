from django.contrib import admin

from contractor.models import Account, Contractor, Address


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    """Админ-панель счетов"""
    list_display = ('id', 'inn', 'number_account')


@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    """Админ-панель поставщик"""
    list_display = ['name', 'address', 'debt',]

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    """Админ-панель счетов"""
    list_display = ['city',]

