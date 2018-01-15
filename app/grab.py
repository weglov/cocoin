import requests
import shutil
import random

from app.models import Coin, CoinShot


URL = "https://api.coinmarketcap.com/v1/ticker"
IMAGE_URL = "https://files.coinmarketcap.com/static/img/coins/128x128/"

def get_coins(url=URL, *params):
	r = requests.get(url, params=params)
	return r.json()

def update_coin_list():
	for coin in get_coins():
		# try:
			item = Coin.objects.update_or_create(
				name=coin['name'],
				defaults={
					'code': coin['symbol'],
					'price': round(float(coin['price_usd']), 3),
					'supply': coin['total_supply'],
					'volume_24h': coin['24h_volume_usd'],
					'market_cap_usd': coin['market_cap_usd'],
					'logo': '{}.png'.format(coin['id'])
				},
			)

			if random.randint(1,25) == 10:
				load_logo(coin['id'])

			CoinShot.objects.create(coin=item[0], value=item[0].price)
		# except:
		# 	print('Error save: {} ({})- {}'.format(coin['name'], coin['symbol'], coin['price_usd']))


def load_logo(id):
	r = requests.get(IMAGE_URL + id + '.png', stream=True)
	if r.status_code == 200:
		with open('uploads/' + id + '.png', 'wb') as out_file:
			shutil.copyfileobj(r.raw, out_file)
	del r