from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^item/(?P<product_id>\w+)/$', views.product, name='product'),
    url(r'^category/(?P<category_name>\w+)/$', views.category, name='category'),
]