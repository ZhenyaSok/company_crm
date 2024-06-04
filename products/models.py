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
    created = models.DateTimeField(auto_now_add=True)

    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                verbose_name='пользователь', **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='статус публикации')


    def __str__(self):
        return f'{self.name} ({self.price})'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('price',)


class Model(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Наименование товара')
    num_version = models.IntegerField(verbose_name='номер модели')
    name_version = models.CharField(max_length=100, verbose_name='название модели')
    version_flug = models.BooleanField(verbose_name='признак модели', default=False)

    def __str__(self):
        return f'{self.product} ({self.name_version})'



    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'