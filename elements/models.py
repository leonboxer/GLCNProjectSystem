from django.db import models
from django.db.models import UniqueConstraint

from materials.models import Material
from tags.models import Tag


class Element(models.Model):
    tag = models.ForeignKey(Tag, related_name='elements', on_delete=models.PROTECT)
    material = models.ForeignKey(Material, related_name='elements', on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        UniqueConstraint(fields=['tag', 'material'], name='unique_element')

    def __str__(self):
        return self.tag.tag_number + "-" + str(self.material)
