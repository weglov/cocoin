from django.contrib.auth.models import User
from .models import Coin, Asset
from app.serializers import UserSerializer, CoinSerializer, AssetSerializer
from rest_framework import mixins, viewsets, generics

from .grab import update_coin_list


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class CoinList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer

    def get(self, request, *args, **kwargs):
        update_coin_list()
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CoinDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer


class AssetsList(generics.CreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
