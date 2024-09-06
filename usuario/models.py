from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Users(AbstractUser):
    username = models.CharField(max_length=15, unique=True, default='default_username')
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

    # Especificamos un related_name único para evitar conflictos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Nombre único para evitar conflictos
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Nombre único para evitar conflictos
        blank=True
    )

    def __str__(self):
        return self.username
