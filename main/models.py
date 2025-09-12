import uuid
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.FloatField(default=0.0)
    views = models.IntegerField(default=0)
    thumbnail = models.URLField()
    category = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    def increment_views(self):
        self.views += 1
        self.save()