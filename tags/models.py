from django.db import models


# Create your models here.
class Tag(models.Model):
    tag_number = models.CharField(max_length=10, blank=False, unique=True)
    description = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tag_number
