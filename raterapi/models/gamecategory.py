"""Gamecategory model module"""
from django.db import models

class Gamecategory(models.Model):
    """Gamecategory database model"""
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
