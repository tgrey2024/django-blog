from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    
    # returns f-string with title from dataset
    def __str__(self):
        return self.title
