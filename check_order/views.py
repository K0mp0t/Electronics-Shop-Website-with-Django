from django.shortcuts import render, HttpResponse
from orders.models import Order, ProductInOrder
from django.http import JsonResponse
from .forms import *

def check_order(request):
    form = CheckOrderForm(request.POST or None)
    print(request)
    if form.is_valid():
        try:
            order_nmb = request.POST.get('nmb')
            order = Order.objects.get(id=order_nmb)
            products_in_order = ProductInOrder.objects.filter(order=order)
            total_price = 0
            total_nmb = products_in_order.count()
            for product in products_in_order:
                total_price += product.total_price
            found = True
        except:
            found = False
        
    return render(request, 'search/check_order.html', locals())

