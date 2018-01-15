import requests
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from app.models import Coin, CoinShot


URL = "https://api.coinmarketcap.com/v1/ticker"
IMAGE_URL = "https://files.coinmarketcap.com/static/img/coins/128x128/"

def get_coins(url=URL, *params):
	r = requests.get(url, params=params)
	return r.json()

def update_coin_list(with_logo=False):
	for coin in get_coins():
		item = Coin.objects.update_or_create(
			name=coin['name'],
			defaults={
				'code': coin['symbol'],
				'rank': coin['rank'],
				'price': round(float(coin['price_usd']), 3),
				'supply': coin['total_supply'],
				'volume_24h': coin['24h_volume_usd'],
				'market_cap_usd': coin['market_cap_usd'],
				'logo': '{}.png'.format(coin['id'])
			},
		)

		if with_logo:
			save_image_from_url(item[0].logo, coin['id']);

		CoinShot.objects.create(coin=item[0], value=item[0].price)

def save_image_from_url(field, id):
    r = requests.get(IMAGE_URL + id + '.png', stream=True)
    if r.status_code == requests.codes.ok:
        img_temp = NamedTemporaryFile(delete = True)
        img_temp.write(r.content)
        img_temp.flush()
        field.save(id + '.png', File(img_temp), save = True)

        return True

    return False
