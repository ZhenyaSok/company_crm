from datetime import time

from django.db import models

from contractor.models import Contractor, NULLABLE
from products.models import Product
from users.models import User


def document_path(self, filename):
    hash_ = int(time.time())
    return "%s/%s/%s" % ("docs", hash_, filename)


class TradeQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(trade.sum() for trade in self)

    def total_quantity(self):
        return sum(trade.quantity for trade in self)

    def stripe_products(self):
        line_items = []
        for trade in self:
            item = {
                'price': trade.product.stripe_product_price_id,
                'quantity': trade.quantity,
            }
            line_items.append(item)
        return line_items


class Trade(models.Model):
    contractor = models.ForeignKey(Contractor, on_delete=models.PROTECT, verbose_name="Поставщик")
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = TradeQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.last_name} | Продукт: {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity

    def de_json(self):
        trade_item = {
            'product_name': self.product.name,
            'quantity': self.quantity,
            'price': float(self.product.price),
            'sum': float(self.sum()),
        }
        return trade_item

    @classmethod
    def create_or_update(cls, product_id, user):
        trades = Trade.objects.filter(user=user, product_id=product_id)

        if not trades.exists():
            obj = Trade.objects.create(user=user, product_id=product_id, quantity=1)
            is_created = True
            return obj, is_created
        else:
            trade = trades.first()
            trade.quantity += 1
            trade.save()
            is_crated = False
            return trade, is_crated





# class Trade(models.Model):
#
#     """Модель сделки"""
#
#     PREPAYMENT = 'Предоплата'
#     POSTPAYD = 'Постоплата'
#
#     STATUS_CHOICES = [
#         (PREPAYMENT, "Предоплата"),
#         (POSTPAYD, "Постоплата"),
#     ]
#     contractor = models.ForeignKey(Contractor, on_delete=models.PROTECT, verbose_name="Поставщик")
#     products = models.ManyToManyField(Product, verbose_name="Товары")
#     quantity = models.PositiveIntegerField(verbose_name="Количество")
#     payment_method = models.CharField(max_length=85, choices=STATUS_CHOICES, verbose_name="Способ оплаты")
#     document_file = models.FileField(upload_to=document_path, max_length=5000, **NULLABLE)
#     payment_summ = models.PositiveIntegerField(verbose_name="Сумма оплаты")
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     is_approved = models.BooleanField(default=False, verbose_name='Одобрение руководителя')
#
#     def all_summ(self):
#
#         """Метод получения всех товаров для отражения названий продуктов в админ-панели"""
#         return ([product.json.price for product.json in self.products.all()]) * self.quantity
#
#     all_summ.short_description = 'Сумма'
#
#     def __str__(self):
#         self.payment_method


    class Meta:
        verbose_name = "Сделка"
        verbose_name_plural = "Сделки"
        db_table = "trades"
