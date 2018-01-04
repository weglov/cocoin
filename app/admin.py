from django.contrib import admin
from .models import Coin


class CoinAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'code', 'price', 'update_date')
    search_fields = ('name',)

admin.site.register(Coin, CoinAdmin)
