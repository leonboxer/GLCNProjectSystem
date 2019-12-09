from django.db import models
from brands.models import Brand


# Create your models here.
class Material(models.Model):
    order_number = models.CharField(max_length=50, blank=False, unique=True)
    type = models.CharField(max_length=50, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='brand')
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, name='update_time')

    def __str__(self):
        return self.order_number + '-' + self.brand.brand_name
