from datetime import timezone

from django.db import models
from brands.models import Brand


# Create your models here.
class Material(models.Model):
    order_number = models.CharField(max_length=50, primary_key=True)
    type = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand')
    created_time = models.DateTimeField(auto_now_add=True, blank=True)
    update_time = models.DateTimeField(auto_now=True, blank=True, name='update_time')

    def __str__(self):
        return self.order_number
