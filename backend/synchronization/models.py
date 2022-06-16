from django.db import models


class Order(models.Model):
    order_number = models.IntegerField(verbose_name='Номер заказа', unique=True, db_index=True)
    delivery_date = models.DateField(verbose_name='Срок поставки')
    price_dollars = models.FloatField(verbose_name='Цена в долларах $')
    price_rubles = models.FloatField(verbose_name='Цена в рублях ₽')

    def __str__(self):
        return str(self.order_number)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
