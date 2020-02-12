from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

class Tutorial(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    published = models.DateTimeField('date published', default=datetime.now)

    def __str__(self):
        return self.title

class Post(models.Model):
    username= models.CharField(max_length=300, unique=True)
    password= models.TextField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    attempts = models.IntegerField(default='0')



               