"""Models of api app."""
from django.db import models


class StartApp(models.Model):
    """Start app model."""

    image = models.ImageField('Лого', upload_to='logo/')
    name = models.CharField('Имя', max_length=1024)
    description = models.TextField('Описание', max_length=100*1024)

    def __str__(self) -> str:
        return self.name
