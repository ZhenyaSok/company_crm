from datetime import time

from django.db import models

from contractor.models import Contractor, NULLABLE
from products.models import Product

def document_path(self, filename):
    hash_ = int(time.time())
    return "%s/%s/%s" % ("docs", hash_, filename)

class Trade(models.Model):

    PREPAYMENT = 'Предоплата'
    POSTPAYD = 'Постоплата'

    STATUS_CHOICES = [
        (PREPAYMENT, "Предоплата"),
        (POSTPAYD, "Постоплата"),
    ]
    contractor = models.ForeignKey(Contractor, on_delete=models.PROTECT, verbose_name="Поставщик")
    products = models.ManyToManyField(Product, verbose_name="Товары")
    quantity = models.PositiveIntegerField(verbose_name="Количество")
    payment_method = models.CharField(max_length=85, choices=STATUS_CHOICES, verbose_name="Способ оплаты")
    document_file = models.FileField(upload_to=document_path, max_length=5000, **NULLABLE)
    payment_summ = models.PositiveIntegerField(verbose_name="Сумма оплаты")

    is_approved = models.BooleanField(default=False, verbose_name='Одобрение руководителя')

    def all_summ(self):

        """Метод получения всех товаров для отражения названий продуктов в админ-панели"""
        return ([product.price for product in self.products.all()]) * self.quantity

    all_summ.short_description = 'Сумма'
