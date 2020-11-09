"""Game model module"""
from django.db import models

class Game(models.Model):
    """Game database model"""
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    duration= models.CharField(max_length=50)
    release_year = models.IntegerField()
    number_of_players = models.IntegerField()
    age_restrictions = models.IntegerField()
    designer = models.ForeignKey("Designer", on_delete=models.CASCADE)
