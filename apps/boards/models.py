from django.core.validators import MinValueValidator
from django.db import models


class BulletinBoard(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=200)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)