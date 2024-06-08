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
    fields = ['name', 'address', 'bank_account', ('provider', 'levels'), 'products', 'debt']
    list_display_links = ('provider',)
    list_filter = ['address']
    search_fields = ['name']
    actions = ['clear_arrears']

    @admin.action(description="Очищение задолженности")
    def clear_arrears(modeladmin, request, queryset):
        queryset.update(arrears=0)

    # def clear_arrears(self, request, queryset):
    #     for item in queryset:
    #         item.debt = 0
    #         item.save()
    #     self.message_user(request, f'Очищение задолженности перед поставщиком.')
    #
    # clear_arrears.short_description = 'Очистить задолженность'


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    """Админ-панель счетов"""
    list_display = ['city',]

