from django.db import models
from django.db.models import UniqueConstraint

from brands.models import Brand


# Create your models here.
class Material(models.Model):
    material_number = models.CharField(max_length=30, blank=False, unique=True)
    order_number = models.CharField(max_length=50, blank=False)
    type = models.CharField(max_length=50, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='materials')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, name='updated')

    class Meta:
        ordering = ('brand', 'created',)
        UniqueConstraint(fields=['brand', 'order_number'], name='unique_material')

    def __str__(self):
        return self.brand.brand_name + '-' + self.type + '(' + self.order_number + ')'
