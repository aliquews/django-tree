from typing import List

from django.db import models

# Create your models here.

class MenuItem(models.Model):
    name = models.CharField(max_length=255, null=False, blank=True)
    url = models.CharField(max_length=255, blank=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='child',
        default=0,
    )

    def __str__(self) -> str:
        return self.name