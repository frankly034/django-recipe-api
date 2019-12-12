from django.db import models

# Create your models here.
class Recipe(models.Model):
  name = models.CharField(max_length=100)
  ingredients = models.CharField(max_length=500, blank=True)
  instructions = models.CharField(max_length=500, blank=True)
  image_url = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
