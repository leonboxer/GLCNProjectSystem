from django.db import models


# Create your models here.
class Brand(models.Model):
    brand_name = models.CharField(max_length=30, primary_key=True)
    description = models.CharField(max_length=100, verbose_name='描述')
    created_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.brand_name
