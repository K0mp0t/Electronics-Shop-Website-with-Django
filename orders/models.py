from django.db import models
from items.models import Product
from django.db.models.signals import post_save
import datetime

class Order(models.Model):
    STATUS_CHOICES = (('В обработке', 'В обработке'), ('Отправлен', 'Отправлен'), ('Выполнен', 'Выполнен'), ('Отменен', 'Отменен'))
    
    customer_name = models.CharField(default=None, blank=True, null=True, max_length=128)
    customer_email = models.EmailField(default=None, blank=True, null=True)
    comments = models.TextField(default=None, blank=True, null=True)
    status = models.CharField(max_length=24, choices=STATUS_CHOICES, default=None, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return 'Заказ № %s' % self.id
    
    class Meta:
        verbose_name='Заказ'
        verbose_name_plural='Заказы'
        
    def save(self, *args, **kwargs):

        super(Order, self).save(*args, **kwargs)
        
class ProductInOrder(models.Model):
    
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, default=None, blank=True, null=True, on_delete=models.CASCADE)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return 'Товар № %s' % self.id
    
    class Meta:
        verbose_name='Товар в заказе'
        verbose_name_plural='Товары в заказе'
    
    def save(self, *args, **kwargs):
        
        price_per_item = self.product.price_w_discount
        self.price_per_item = price_per_item
        self.total_price = self.nmb * price_per_item

        super(ProductInOrder, self).save(*args, **kwargs)

def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.order.total_amount = order_total_price
    instance.order.save(force_update=True)

post_save.connect(product_in_order_post_save, sender=ProductInOrder)