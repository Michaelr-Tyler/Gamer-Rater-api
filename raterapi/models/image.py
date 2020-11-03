"""Image model module"""
from django.db import models

class Image(models.Model):
    """Image database model"""
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
