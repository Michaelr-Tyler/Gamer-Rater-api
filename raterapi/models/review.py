"""Review model module"""
from django.db import models

class Review(models.Model):
    """Review database model"""
    comment = models.CharField(max_length=250)
    rating = models.IntegerField()
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
