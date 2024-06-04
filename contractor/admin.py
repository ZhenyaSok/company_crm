from django.contrib import admin

from contractor.models import Account, Contractor


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    """Админ-панель счетов"""
    list_display = ('id', 'name', 'inn', 'number_account')


@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    """Админ-панель поставщик"""
    list_filter = ['city', 'level']
    list_display = ['name', 'city', 'debt', 'level']

