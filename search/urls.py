from django.conf.urls import include, url
from . import views

app_name = 'search'

urlpatterns = [
    url(r'^search/$', views.ESearchView.as_view(), name = 'index'),
]