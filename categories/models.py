from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=500, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
