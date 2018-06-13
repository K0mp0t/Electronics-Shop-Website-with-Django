from django.shortcuts import render
from items.models import *
import decimal

def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True) 
    
    return render(request, 'landing/home.html', locals())
