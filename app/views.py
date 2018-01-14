from django.contrib.auth.models import User
from .models import Coin, Asset, CoinShot
from app.serializers import CoinSerializer, AssetSerializer, CoinShotSerializer
from rest_framework import mixins, generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import datetime


from .grab import update_coin_list

class CoinList(ModelViewSet):
    authentication_classes = (TokenAuthentication, JSONWebTokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Coin.objects.all().order_by('-price')[:50]
    serializer_class = CoinSerializer

    def list(self, request, *args, **kwargs):
        return ModelViewSet.list(self, request, *args, **kwargs)
    
    def retrieve(self, request, pk=None, *args, **kwargs):
        date_from = datetime.datetime.now() - datetime.timedelta(days=1)
        queryset = CoinShot.objects.filter(coin=pk, published_date__gte=date_from).order_by('-published_date')
        serializer = CoinShotSerializer(queryset, many=True)

        return Response(serializer.data)


class AssetsList(generics.CreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

