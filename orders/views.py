from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from items.models import Product, ProductImage
from .models import ProductInCart, Order, ProductInOrder
from .forms import CheckoutContactForm

def cart_update(request):
    return_dict = dict();
    purpose = request.POST['purpose']
    if purpose == '+':
        product_id = request.POST['product_id']
        nmb = int(request.POST['nmb'])
        price_w_discount = Product.objects.get(id=product_id).price_w_discount
        total_price = price_w_discount * nmb
        session_key = request.session.session_key
        if not session_key:
            request.session["session_key"] = 123
            request.session.cycle_key()
        new_product, created = ProductInCart.objects.get_or_create(session_key=session_key, product=Product.objects.get(id=product_id), defaults={"nmb": nmb})
        if not created:
            new_product.nmb += nmb
            new_product.save(force_update=True)
        products_in_cart = ProductInCart.objects.filter(session_key=request.session.session_key)
        total_nmb = products_in_cart.count()
        total_price = 0
        for product in products_in_cart:
            total_price += product.total_price
        return_dict['total_nmb'] = total_nmb
        return_dict['total_price'] = total_price
    if purpose == '-':
        product_id = request.POST['id']
        product_on_delete = ProductInCart.objects.get(id=product_id)
        return_dict['id'] = product_on_delete.product.id
        product_on_delete.delete()
        products_in_cart = ProductInCart.objects.filter(session_key=request.session.session_key)
        total_nmb = products_in_cart.count()
        total_price = 0
        for product in products_in_cart:
            total_price += product.total_price
        return_dict['total_nmb'] = total_nmb
        return_dict['total_price'] = total_price

    return JsonResponse(return_dict)

def cart(request):
    cart_items = ProductInCart.objects.filter(session_key=request.session.session_key)
    total_nmb = cart_items.count()
    total_price = 0
    for item in cart_items:
        total_price += item.total_price
    
    return render(request, 'orders/cart.html', locals())

# def new_order(request):
#     customer_contacts = request.POST.dict()
#     new_order = Order.objects.create(customer_name=customer_contacts['name'], customer_email=customer_contacts['email'], customer_phone=customer_contacts['phone'], status='В обработке', total_amount=total_price)
#     for item in cart_items:
#         print(item.nmb, type(item.nmb))
#         ProductInOrder.objects.create(order=new_order, product=Product.objects.get(id=item.product.id), nmb=item.nmb)
#     cart_items = ProductInCart.objects.filter(session_key=session_key)
#     return render(request, 'landing/home.html', locals())
    
def pre_make_order(request):
    session_key = request.session.session_key
    if request.POST:
        cart_items_update = request.POST.dict()
        cart_items_update.pop('csrfmiddlewaretoken')
        for cart_item in cart_items_update:
            item = ProductInCart.objects.get(session_key=session_key, product=Product.objects.get(id=cart_item))
            item.nmb = int(cart_items_update.get(cart_item))
            item.save(force_update=True)
    
    return HttpResponse('')

def make_order(request):
    session_key = request.session.session_key
    form = CheckoutContactForm(request.POST or None)
    cart_items = ProductInCart.objects.filter(session_key=session_key)
    total_price = 0
    for item in cart_items:
        total_price += item.total_price
    if request.POST and form.is_valid():
        customer_contacts = request.POST.dict()
        new_order = Order.objects.create(customer_name=customer_contacts['name'], customer_email=customer_contacts['email'], customer_phone=customer_contacts['phone'], comments=customer_contacts['comments'], status='В обработке', total_amount=total_price)
        for item in cart_items:
            ProductInOrder.objects.create(order=new_order, product=Product.objects.get(id=item.product.id), nmb=item.nmb)
            item.delete()
        cart_items = ProductInCart.objects.filter(session_key=session_key)
        
        products_images = ProductImage.objects.filter(is_active=True, is_main=True)  # need for render
        alert = True
        order_id = new_order.id
        
        return render(request, 'landing/home.html', locals())

    return render(request, 'orders/make_order.html', locals())