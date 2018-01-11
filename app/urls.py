from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as rest_framework_views
from app import views

app_name = 'app'

urlpatterns = [
    url(r'^coins/$', views.CoinList.as_view(), name='coinslist'),
    url(r'^coins/(?P<pk>[0-9]+)/$', views.CoinDetail.as_view(), name='coins_details'),
    url(r'^assets/$', views.AssetsList.as_view(), name='assets_details'),
    url(r'^login/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
]
