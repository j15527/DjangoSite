from .models import Asset
from nomics import Nomics
from celery import shared_task

MY_NOMICS_KEY = "6fefbc3e132ad0009443f5be19ce5a3a"
nomics = Nomics(MY_NOMICS_KEY)
coins = nomics.Currencies.get_currencies(ids="BTC, DOT, ETH, LTC, XRP")

coins.sort(key=lambda item: item.get('id'))

# assets = Asset.objects.all()
assets = Asset.objects.order_by('asset_symbol')

# i = 1
# while i < len(coins):
# Asset.objects.filter(id=i).update(asset_price=coins[i-1]['price'])

# for asset in assets.order_by("asset_symbol"):
# Asset.objects.filter(asset_symbol=asset).update(asset_price=coin['price'])

'''
assets[0].asset_price
coins[0]['price']

id: 1 btc
2 dot
3 eth
4 ltc
5 xrp
'''
