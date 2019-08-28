from django.db import models
from materials.models import Material


# Create your models here.
class Module(models.Model):
    module_name = models.CharField(max_length=50)
    included_material = models.ManyToManyField(Material, 'included_material')
    created_time = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.module_name
