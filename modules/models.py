from django.db import models
from materials.models import Material
from tags.models import Tag
from elements.models import Element


# Create your models here.
class ModuleName(models.Model):
    description = models.CharField(max_length=30)

    def __str__(self):
        return self.description


class Module(models.Model):
    module_name = models.ForeignKey(ModuleName, on_delete=models.CASCADE)
    element = models.ManyToManyField(Element)
    created_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)

    # tag = models.ManyToManyField(Tag, related_name='included_tag_number')

    def __str__(self):
        return self.module_name.description
