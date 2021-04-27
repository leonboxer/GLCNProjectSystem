from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    Admin = 'admin'
    Editor = 'editor'
    ROLES_CHOICES = [
        (Admin, 'admin'),
        (Editor, 'editor'),
    ]
    roles = models.CharField(
        max_length=10,
        choices=ROLES_CHOICES,
        default=Admin,
    )
    name = models.CharField(max_length=20, blank=True, null=True, name='name')
    avatar = models.ImageField(blank=True, null=True,name='avatar')
    introduction = models.TextField(max_length=100, blank=True, name='introduction')

    class Meta:
        db_table = 'userinfo'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
