from datetime import timezone

from django.db import models


# Create your models here.
class Material(models.Model):
    brand = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    created_time = models.DateTimeField(auto_now_add=True, blank=True)
    update_time = models.DateTimeField(auto_now=True, blank=True, name='update_time')

    def __str__(self):
        return self.type
