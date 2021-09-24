from django.db import models
from elements.models import Element
from modules.models import Module
from materials.models import Material


class MachineryType(models.Model):
    description = models.CharField(max_length=20)
    created_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description


# Create your models here.
class Project(models.Model):
    project_number = models.CharField(max_length=20, name='project_number')
    machinery_type = models.ForeignKey(MachineryType, on_delete=models.CASCADE)
    elements = models.ManyToManyField(Element, related_name='projects')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.project_number
