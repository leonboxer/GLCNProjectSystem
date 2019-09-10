from django.db import models


# Create your models here.
class Brand(models.Model):
    brand_name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, verbose_name='描述')
