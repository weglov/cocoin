from django.contrib import admin
from .models import Coin


class CoinAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'code', 'price')
    search_fields = ('name',)

admin.site.register(Coin, CoinAdmin)
