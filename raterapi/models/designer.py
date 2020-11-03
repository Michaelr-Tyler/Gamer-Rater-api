"""Designer model module"""
from django.db import models

class Designer(models.Model):
    """Designer database model"""
    Name = models.CharField(max_length=50)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
