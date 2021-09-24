from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    """
    The Role entries are managed by the system,
    automatically created via a Django data migration.
    """
    ADMIN = 1
    EDITOR = 2
    USER = 3
    SUPEREDITOR = 4
    ROLE_CHOICES = (
        (ADMIN, 'admin'),
        (EDITOR, 'editor'),
        (USER, 'user'),
        (SUPEREDITOR, 'super editor'),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return str(self.get_id_display())


class User(AbstractUser):
    roles = models.ManyToManyField(Role)
    name = models.CharField(max_length=20, blank=True, null=True, name='name')
    avatar = models.ImageField(blank=True, null=True, name='avatar', upload_to='avatars')
    introduction = models.TextField(max_length=100, blank=True, name='introduction')

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('user-detail', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'userinfo'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
