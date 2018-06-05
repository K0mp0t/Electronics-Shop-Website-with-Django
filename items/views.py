from django.shortcuts import render
from . import models

def item(request):
    
    return render(request, 'items/item.html', locals())
