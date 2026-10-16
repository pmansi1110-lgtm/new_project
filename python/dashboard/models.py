from django.db import models

# Create your models here.

class Product(models.Model):
    image = models.ImageField(upload_to='product_images/')
    name = models.CharField(max_length=100)
    description = models.TextField()
    old_price = models.IntegerField()
    new_price = models.IntegerField()