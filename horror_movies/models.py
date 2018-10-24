from django.db import models
from uuid import uuid4
# Create your models here.

class Movies(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    title = models.CharField(max_length = 200)
    content = models.TextField(blank = True)
    review = models.TextField(blank = True)
    RottenTomatoes = models.URLField(blank=True)
    url = models.URLField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class Announcement(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    title = models.CharField(max_length = 200)
    content = models.TextField(blank = True)
       
