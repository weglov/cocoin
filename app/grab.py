import requests
from app.models import Coin


URL = "https://api.coinmarketcap.com/v1/ticker/"

def get_coins(url=URL, *params):
	r = requests.get(url, params=params)
	return r.json()

def update_coin_list():
	for coin in get_coins():
		item = Coin.objects.update_or_create(
			name=coin['name'],
			defaults={
				'code': coin['symbol'],
				'price': coin['price_usd'],
			},
		)

if __name__ == "__main__":
	update_coin_list()