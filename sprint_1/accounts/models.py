from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files.uploadedfile import InMemoryUploadedFile


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

class Profile(models.Model):
    Accountant = 1
    Manager = 2
    Admin = 3
    ROLE_CHOICES = (
        (Accountant, 'Accountant'),
        (Manager, 'Manager'),
        (Admin, 'Admin'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_initial = models.CharField(max_length=1, blank=True)
    dob = models.DateField(null=True, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    state = models.CharField(max_length=30, null=True, blank=True)
    zip_code = models.CharField(max_length=5, null=True, blank=True)
    image = models.ImageField(upload_to='profile_image', null=True, blank=True)
    bio = models.TextField(max_length=500, null = True, blank=True)


active = models.BooleanField(default=True)
staff = models.BooleanField(default=True)
superuser = models.BooleanField(default=True)

@property
def is_superuser(self):
    return self.superuser

@property
def is_active(self):
    return self.active

@property
def is_staff(self):
    return self.active


               