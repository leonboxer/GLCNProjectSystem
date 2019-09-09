from django.db import models
from modules.models import Module
from materials.models import Material


# Create your models here.
class Project(models.Model):
    project_number = models.CharField(max_length=20,name='project_number')
    machinery_type = models.CharField(max_length=10)
    included_module = models.ManyToManyField(Module, 'included_module')

    # included_material = models.ManyToManyField(Material, 'project_included_material')
    created_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_number
