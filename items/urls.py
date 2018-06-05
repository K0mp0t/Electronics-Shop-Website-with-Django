from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^item/$', views.item, name='item')
]