from django.contrib import admin
from .models import Coin, Asset, CoinShot


class CoinAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'code', 'price', 'update_date')
    search_fields = ('name',)

class CoinShotAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'published_date', 'value')
    search_fields = ('name',)

admin.site.register(Coin, CoinAdmin)
admin.site.register(Asset)
admin.site.register(CoinShot, CoinShotAdmin)
