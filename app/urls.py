from django.urls import path
from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
from app import views

router = DefaultRouter()
router.register(r'coins', views.CoinList)

app_name = 'app'

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^coins/(?P<pk>[0-9]+)/$', views.CoinDetail.as_view(), name='coins_details'),
    url(r'^assets/$', views.AssetsList.as_view(), name='assets_details'),
     url(r'^login/', obtain_jwt_token),
]
