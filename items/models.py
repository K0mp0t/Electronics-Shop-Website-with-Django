from django.db import models
import datetime
import decimal

class ProductCategory(models.Model):
    name = models.CharField(max_length=16, blank=True, null=True, default=None)
    
    def __str__(self):
        return '%s' % self.name
    
    class Meta:
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'

class Product(models.Model):
    
    name = models.CharField(max_length=128, default=None, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.SET_NULL)
    discount = models.IntegerField(blank=True, null=True, default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_w_discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return '%s, %s' % (self.price_w_discount, self.name)
    
    def save(self, *args, **kwargs):
        d = decimal.Decimal(self.discount/100)
        self.price_w_discount = self.price * (1 - d)
        self.price_w_discount = self.price_w_discount.quantize(decimal.Decimal("1.00"))
        
        super(Product, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        
class ProductImage(models.Model):
    
    product = models.ForeignKey(Product, default=None, blank=True, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'