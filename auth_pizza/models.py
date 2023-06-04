from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    nombre = models.CharField('Nombre', max_length=300)

    class Meta:
        ordering = ['-is_active', 'username']

    def __str__(self):
        if not self.nombre:
            return self.username
        return self.nombre

    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)

