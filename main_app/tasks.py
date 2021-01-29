# from celery.task.schedules import crontab
# from celery.decorators import periodic_task
# from celery.utils.log import get_task_logger
from .models import Asset
from nomics import Nomics

# logger = get_task_logger(__name__)

MY_NOMICS_KEY = "6fefbc3e132ad0009443f5be19ce5a3a"
nomics = Nomics(MY_NOMICS_KEY)
coins = nomics.Currencies.get_currencies(ids="BTC, DOT, ETH, LTC, XRP")

coins.sort(key=lambda item: item.get('id'))

# assets = Asset.objects.all()
assets = Asset.objects.order_by('asset_symbol')

'''
@periodic_task(
    run_every=(crontab(minutes='*/1')),
    name="db_update",
    ignore_result=True
)

'''


def db_update():
    Asset.objects.filter(id=1).update(asset_price=coins[0]['price'])
    Asset.objects.filter(id=2).update(asset_price=coins[1]['price'])
    Asset.objects.filter(id=3).update(asset_price=coins[2]['price'])
    Asset.objects.filter(id=4).update(asset_price=coins[3]['price'])
    Asset.objects.filter(id=5).update(asset_price=coins[4]['price'])
    # logger.info("Update complete")
