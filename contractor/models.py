from django.db import models
from django.utils.translation import gettext_lazy as _

from contractor.utils import COUNTRIES
from products.models import Product

NULLABLE = {'null': True, 'blank': True}


class Address(models.Model):

    email = models.EmailField(verbose_name="Почта", unique=True)
    country = models.CharField(max_length=3, choices=COUNTRIES, verbose_name="Страна", default="")
    city = models.CharField(max_length=150, verbose_name="Город", default="")
    street = models.CharField(max_length=55, verbose_name="Улица", default="")
    house_number = models.CharField(max_length=15, verbose_name="Номер дома", default="")


    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"
        db_table = "address"


    def __str__(self):
        return self.country if self.country else ""

    def get_complete_address(self):
        address = ""
        if self.country:
            if address:
                address = self.country
        if self.city:
            if address:
                address += f", {self.city}"
            else:
                address += self.city
        if self.street:
            if address:
                address += f", {self.street}"
            else:
                address += self.street

        if self.house_number:
            if address:
                address += f", {self.house_number}"
            else:
                address += self.house_number

        return address


class Account(models.Model):
    """
    Модель банковского счета(поля с учетом требований РФ)
    """

    name = models.ManyToManyField("Contractor", verbose_name="Название компании")
    inn = models.PositiveIntegerField(verbose_name="ИНН")
    ogrn_ogrnip = models.PositiveIntegerField(verbose_name="ОГРН/ОГРИП")
    number_account = models.PositiveIntegerField(verbose_name="Расчетный счет")
    banks_name = models.CharField(max_length=450, verbose_name="Название банка")
    сorr_acc = models.PositiveIntegerField(verbose_name="Корреспондентский счет банка")
    bic = models.PositiveIntegerField(verbose_name="Банковский идентификационный код")
    kpp = models.PositiveIntegerField(verbose_name="КПП банка")

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"
        db_table = "accounts"


    def __str__(self):
        return f"{self.name}"


class Levels(models.IntegerChoices):
    """Уровни поставщиков"""

    FACTORY = 0, 'Завод'
    RETAIL_NETWORK = 1, 'Розничная сеть'
    BUSINESSMAN = 2, 'Предприниматель'

class Contractor(models.Model):
    """Модель контрагента (поставщика, компании)"""

    name = models.CharField(max_length=150, verbose_name="Название контрагента")
    email = models.EmailField(verbose_name="Почта", unique=True)
    address = models.ForeignKey("Address", on_delete=models.CASCADE, **NULLABLE)
    bank_account = models.ForeignKey(
        "Account",
        on_delete=models.CASCADE,
        verbose_name="номер счета", default="не назначен")
    products = models.ManyToManyField(Product, verbose_name='Продукт')
    provider = models.ForeignKey('self', on_delete=models.PROTECT, verbose_name='Поставщик', **NULLABLE)

    levels = models.IntegerField(choices=Levels.choices, default=Levels.FACTORY, verbose_name='Уровень поставщика')
    debt = models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Задолженность', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = "Контрагент"
        verbose_name_plural = "Контрагенты"
        db_table = "Contractors"
        ordering = ("-created_at",)

    def __str__(self):
        return str(self.name)


