"""models.py"""
from django.db import models


class BaseModel(models.Model):
    """
    Base model for all models.
    """
    class Meta:
        """Meta class"""
        abstract = True

    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
