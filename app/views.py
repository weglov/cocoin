from django.contrib.auth.models import User
from .models import Coin
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from app.serializers import UserSerializer, CoinSerializer

from .grab import update_coin_list


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class CoinList(APIView):
    def get(self, request, format=None):
        update_coin_list()  #temporary decision
        coins = Coin.objects.all()
        serializer = CoinSerializer(coins, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CoinSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
