from django.shortcuts import render

def order(request):
    
    return render(request, 'orders/orders.html', locals())
