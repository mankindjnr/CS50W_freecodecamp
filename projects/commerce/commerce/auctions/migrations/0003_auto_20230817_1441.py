# Generated by Django 3.0.8 on 2023-08-17 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auction_listing_bids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_listing',
            name='image_url',
            field=models.URLField(max_length=500),
        ),
    ]