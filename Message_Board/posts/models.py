from django.db import models
from django.db.models import TextField


class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:10]
