from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class auction_listing(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    min_bid = models.IntegerField()
    category = models.CharField(max_length=100)
    image_url = models.URLField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    # add time later

    def __str__(self):
        return f"{self.title} listed at {self.timestamp.strftime('%B %d, %Y %H:%M:%S')}"


class bids(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    bid_amount = models.IntegerField()
    product = models.CharField(max_length=100)


class comments(models.Model):
    pass