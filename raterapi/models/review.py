"""Review model module"""
from django.db import models
from django.utils import timezone


class Review(models.Model):
    """Review database model"""
    comment = models.CharField(max_length=250)
    rating = models.IntegerField()
    timestamp = models.DateTimeField(default=timezone.now())
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
