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
    )
    is_active = models.BooleanField(default=False)