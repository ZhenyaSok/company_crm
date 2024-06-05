from django.db import models
from django.utils import timezone

from config import settings

NULLABLE = {'null': True, 'blank': True}

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')
    description = models.TextField(**NULLABLE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'



class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование товара')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    photo = models.ImageField(upload_to='catalog/', verbose_name='Изображение', **NULLABLE)
    price = models.FloatField(default=0, verbose_name='Цена за штуку')
    overview = models.TextField(verbose_name='Описание', **NULLABLE)
    model_product = models.CharField(max_length=100, verbose_name='Модель')
    created_at = models.DateField(auto_now_add=True)

    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                verbose_name='пользователь', **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='статус публикации')


    def __str__(self):
        return f'{self.name} {self.created_at} {self.model_product} ({self.price})'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('price',)
