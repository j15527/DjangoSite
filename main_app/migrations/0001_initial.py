# Generated by Django 3.1.5 on 2021-01-26 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_symbol', models.CharField(default='', max_length=20)),
                ('asset_price', models.FloatField(default=0)),
                ('asset_name', models.CharField(default='', max_length=20)),
                ('asset_high', models.FloatField(default=0)),
                ('asset_1d_price_change', models.FloatField(default=0)),
                ('asset_volume', models.FloatField(default=0)),
                ('asset_count', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('net_worth', models.FloatField(default=0)),
                ('assets', models.ManyToManyField(blank=True, to='main_app.Asset')),
            ],
        ),
    ]