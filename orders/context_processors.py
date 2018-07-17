from .models import ProductInCart

def getting_cart_info(request):

    session_key = request.session.session_key
    if not session_key:
        request.session["session_key"] = 123
        request.session.cycle_key()
    products_in_cart = ProductInCart.objects.filter(session_key=request.session.session_key)
    total_nmb = products_in_cart.count()
    total_price = 0
    for product in products_in_cart:
        total_price += product.total_price
    return locals()