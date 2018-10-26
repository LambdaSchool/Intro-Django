from django.db import models
from uuid import uuid4

from django.contrib.auth.models import User 


# Create your models here.
class Topic(models.Model):
   """A topic the user is learning about"""
   id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
   title = models.CharField(max_length=200, default='')
   text = models.CharField(max_length=200)

   created_at = models.DateTimeField(auto_now_add=True)
   last_modified = models.DateTimeField(auto_now=True)


class PersonalTopic(Topic):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   
 
   

   

  
