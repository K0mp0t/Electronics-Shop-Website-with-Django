from django.shortcuts import render
from .models import *

def product(request, product_id):
    product = Product.objects.get(id=product_id)
    main_product_image = ProductImage.objects.get(is_main=True, product=product)
    product_images = ProductImage.objects.filter(is_active=True, product=product, is_main=False)
    
    return render(request, 'items/item.html', locals())

def category(request, category_name):
    category = ProductCategory.objects.get(name=category_name)
    products = Product.objects.filter(category=category)
    product_images = []
    for product in products:
        product_images.append(ProductImage.objects.get(is_main=True, product=product))
    
    return render(request, 'items/category.html', locals())
