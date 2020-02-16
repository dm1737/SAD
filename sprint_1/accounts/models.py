from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

               