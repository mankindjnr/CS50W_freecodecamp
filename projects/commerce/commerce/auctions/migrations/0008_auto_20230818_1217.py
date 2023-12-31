# Generated by Django 3.0.8 on 2023-08-18 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20230818_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='bids',
            name='bid_amount',
            field=models.IntegerField(default=94000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bids',
            name='bidder',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bids',
            name='product',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bids',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
