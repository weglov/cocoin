from django.contrib.auth.models import User
from .models import Coin, Asset
from rest_framework import serializers
from rest_framework.authtoken.models import Token



class AuthorizationSerializer(serializers.HyperlinkedModelSerializer):
    token = serializers.SerializerMethodField()

    def get_token(self, obj):
        token = Token.objects.filter(user=obj.owner).first()
        return token.key if token else None

class CoinSerializer(AuthorizationSerializer):
    class Meta:
        model = Coin
        fields = ('id', 'name', 'code', 'price', 'logo', 'update_date', 'published_date')

class AssetSerializer(AuthorizationSerializer):
    class Meta:
        model = Asset
        fields = ('id', 'owner', 'coin', 'value')