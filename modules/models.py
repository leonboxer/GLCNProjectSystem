from django.db import models
from materials.models import Material


# Create your models here.
class Module(models.Model):
    module_name = models.CharField(max_length=50)
    # slug = models.SlugField(max_length=250,unique_for_date='created_time')
    included_material = models.ManyToManyField(Material, 'included_material')
    created_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.module_name
