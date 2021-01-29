from django.db import models
import json
import requests


class Asset(models.Model):
    asset_symbol = models.CharField(max_length=20, default="")
    asset_price = models.FloatField(default=0)
    asset_name = models.CharField(max_length=20, default="")
    asset_high = models.FloatField(default=0)
    asset_1d_price_change = models.FloatField(default=0)
    asset_volume = models.FloatField(default=0)
    asset_count = models.FloatField(default=0)

    def __str__(self):
        return f"Name: {self.asset_symbol} price: {self.asset_price}"


class Portfolio(models.Model):
    name = models.CharField(max_length=20)
    assets = models.ManyToManyField(Asset, blank=True)
    net_worth = models.FloatField(default=0)

    def net_holdings(self):
        return self.net_worth * self.assets.count

    def __str__(self):
        return f"Name: {self.name} Worth:{self.assets}"
