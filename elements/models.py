from django.db import models
from materials.models import Material
from tags.models import Tag


class Element(models.Model):
    element_tag = models.ForeignKey(Tag, on_delete=models.PROTECT)
    element_material = models.ForeignKey(Material, on_delete=models.PROTECT)

    def __str__(self):
        return self.element_tag.tag_number + "-" + self.element_material.order_number
