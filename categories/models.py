from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(verbose_name="Categoría", max_length=15)