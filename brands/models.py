from django.db import models


# Create your models here.
class Brand(models.Model):
    brand_name = models.CharField(max_length=30, blank=False, unique=True)
    description = models.CharField(max_length=100, verbose_name='描述')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('brand-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ('brand_name',)

    def __str__(self):
        return self.brand_name
