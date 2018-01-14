import requests
from app.models import Coin, CoinShot


URL = "https://api.coinmarketcap.com/v1/ticker/"

def get_coins(url=URL, *params):
	r = requests.get(url, params=params)
	return r.json()

def update_coin_list():
	for coin in get_coins():
		try:
			item = Coin.objects.update_or_create(
				name=coin['name'],
				defaults={
					'code': coin['symbol'],
					'price': round(float(coin['price_usd']), 3),
					'supply': coin['total_supply'],
					'volume_24h': coin['24h_volume_usd'],
					'market_cap_usd': coin['market_cap_usd'],
				},
			)

			CoinShot.objects.create(coin=item[0], value=item[0].price)
		except:
			print('Error save: {} ({})- {}'.format(coin['name'], coin['symbol'], coin['price_usd']))
