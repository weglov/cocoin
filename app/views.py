from django.contrib.auth.models import User
from .models import Coin, Asset, CoinShot
from app.serializers import CoinSerializer, AssetSerializer, CoinShotSerializer
from rest_framework import mixins, generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend


from .grab import update_coin_list


class CoinList(ModelViewSet):
    serializer_class = CoinSerializer
    filter_backends = (DjangoFilterBackend,)

    def list(self, request, *args, **kwargs):
        return ModelViewSet.list(self, request, *args, **kwargs)
    
    def retrieve(self, request, pk=None, *args, **kwargs):
        date_from = timezone.now() - timezone.timedelta(days=1)
        queryset = CoinShot.objects.filter(coin=pk, published_date__gte=date_from).order_by('published_date')
        serializer = CoinShotSerializer(queryset, many=True)

        return Response(serializer.data)

    def get_queryset(self):
        queryset = Coin.objects.all().order_by('-price')
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset[:50]


class WalletViewSet(ModelViewSet):
    authentication_classes = (TokenAuthentication, JSONWebTokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

    def list(self, request, *args, **kwargs):
        queryset = Asset.objects.filter(owner=request.user)
        serializer = AssetSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        coin_istance = Coin.objects.filter(id=request.data['coin'])[0]
        coin = Asset.objects.create(owner=request.user, value=request.data['value'], coin=coin_istance)
        serializer = AssetSerializer(coin)

        return Response(serializer.data)


