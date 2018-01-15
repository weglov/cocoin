from django.db import models
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Coin(models.Model):
    name = models.CharField('Name', max_length=100, unique=True)
    code = models.CharField('Code', max_length=10)
    rank = models.IntegerField(null=True, blank=True)
    price = models.DecimalField('Price', default=0, decimal_places=3, max_digits=16)
    logo = models.ImageField('Logo', upload_to='coins/', null=True, blank=True)
    market_cap_usd = models.DecimalField('Market cap', default=0, decimal_places=2, max_digits=16)
    volume_24h = models.DecimalField('Volume 24', default=0, decimal_places=2, max_digits=16)
    supply = models.DecimalField('Total Supply', default=0, decimal_places=2, max_digits=16)
    update_date = models.DateTimeField('Update date', auto_now=True)
    published_date = models.DateTimeField('Create date', auto_now_add=True)

    def __str__(self):
        return self.name

class CoinShot(models.Model):
    coin = models.ForeignKey('Coin', on_delete=models.CASCADE)
    value = models.DecimalField('Value', default=0, decimal_places=3, max_digits=16)
    published_date = models.DateTimeField('Create date', auto_now_add=True)

    def __str__(self):
        return str(self.id)

class Asset(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    coin = models.ForeignKey('Coin', on_delete=models.CASCADE)
    value = models.DecimalField('Value', decimal_places=8, max_digits=16)
    update_date = models.DateTimeField('Update date', auto_now=True)
    published_date = models.DateTimeField('Create date', auto_now_add=True)

    def __str__(self):
        return '{} - {} ({})'.format(self.owner, self.coin, self.value)
