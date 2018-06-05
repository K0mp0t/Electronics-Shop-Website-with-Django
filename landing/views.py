from django.shortcuts import render
from items.models import *
import decimal

def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True) 
    # for product_image in products_images:
    #     if product_image.product.discount != 0:
    #         d = decimal.Decimal(product_image.product.discount/100)
    #         product_image.product.price_w_discount = product_image.product.price * (1 - d)
    #         product_image.product.price_w_discount = product_image.product.price_w_discount.quantize(decimal.Decimal("1.00"))
    #         product_image.product.save()
    #     if product_image.product.discount == 0:
    #         product_image.product.price_w_discount = product_image.product.price
    #         product_image.product.save()
    
    return render(request, 'landing/home.html', locals())
