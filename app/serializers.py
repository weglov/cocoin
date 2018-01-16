from django.contrib.auth.models import User
from .models import Coin, Asset, CoinShot
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.utils import timezone


class AuthorizationSerializer(serializers.HyperlinkedModelSerializer):
    token = serializers.SerializerMethodField()

    def get_token(self, obj):
        token = Token.objects.filter(user=obj.owner).first()
        return token.key if token else None

class CoinSerializer(AuthorizationSerializer):
    price = serializers.FloatField()
    change_24 = serializers.SerializerMethodField()

    class Meta:
        model = Coin
        fields = ('id', 'name', 'code', 'price', 'logo', 'update_date', 'published_date', 'change_24')
    
    def get_change_24(self, instance):
        try:
            date_from = timezone.now() - timezone.timedelta(days=1)
            data = CoinShot.objects.order_by('-published_date').filter(coin=instance, published_date__gte=date_from)
            previous = data.last()
            current = data.first()

            result = round((current.value - previous.value)/previous.value, 4)
        except:
            result = 0

        return result


class AssetSerializer(AuthorizationSerializer):
    coin = CoinSerializer()
    value = serializers.FloatField()

    class Meta:
        model = Asset
        fields = ('id', 'coin', 'value')


class CoinShotSerializer(AuthorizationSerializer):
    value = serializers.FloatField()

    class Meta:
        model = CoinShot
        fields = ('id', 'value', 'published_date')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user