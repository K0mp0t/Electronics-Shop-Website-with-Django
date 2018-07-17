from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^check_order/$', views.check_order, name='check_order'),
]