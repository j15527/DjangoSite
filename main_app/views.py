
from django.shortcuts import render
from django.http import HttpResponse, request
import json
import requests
from .models import Portfolio
from nomics import Nomics
from . import tasks
from main_app.models import Asset


KEY = "key=6fefbc3e132ad0009443f5be19ce5a3a"
MY_NOMICS_KEY = "6fefbc3e132ad0009443f5be19ce5a3a"
URL = f"https://api.nomics.com/v1/currencies/ticker?{KEY}&interval=1d,30d&per-page=100&page=1"


def index(request):
    api_request = requests.get(URL)  # type class requests.models.Response
    # coins = nomics.Currencies.get_currencies(ids="BTC, ETH")
    results = Asset.objects.all()
    tasks.db_update()
    try:
        api = json.loads(api_request.content)  # type list
        # markets = nomics.Markets.get_markets(exchange='binance')
        # api_request.content type bytes
        # api = api_request.json()# list
    except Exception as e:
        api = "Error..."
    return render(request, "base.html", {"api": api[0], "results": results})
