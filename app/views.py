from django.contrib.auth.models import User
from .models import Coin, Asset
from app.serializers import UserSerializer, CoinSerializer, AssetSerializer
from rest_framework import mixins, generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated


from .grab import update_coin_list


class UserViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class CoinList(ModelViewSet):
    authentication_classes = (TokenAuthentication, JSONWebTokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer

    def list(self, request, *args, **kwargs):
        return ModelViewSet.list(self, request, *args, **kwargs)

class CoinDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer


class AssetsList(generics.CreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

