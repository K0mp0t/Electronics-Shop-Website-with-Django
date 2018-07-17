from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^cart/$', views.cart, name = 'cart'),
    url(r'^cart_update/$', views.cart_update, name = 'cart_update'),
    url(r'^make_order/$', views.make_order, name = 'make_order'),
    url(r'^pre_make_order/$', views.pre_make_order, name='pre_make_order'),
]