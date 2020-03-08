from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.validators import MaxValueValidator, MinValueValidator
from simple_history.models import HistoricalRecords


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
    attempts = models.IntegerField(default=0, blank = True)

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
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class UserAccount (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=300, unique=True)
    account_number = models.PositiveIntegerField(unique=True)
    account_description = models.TextField()
    account_category = models.CharField(max_length=300)
    account_subcategory = models.CharField(max_length=300)
    initial_balance = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(0)])
    debit = models.DecimalField(decimal_places=2, max_digits=10)
    credit = models.DecimalField(decimal_places=2, max_digits=10)
    balance = models.DecimalField(decimal_places=2, max_digits=10)
    account_created = models.DateTimeField(default=datetime.now)
    order = models.CharField(max_length=300)
    statement = models.FileField(null=True)
    comment = models.TextField()
    history = HistoricalRecords()


    def __str__(self):
        return self.account_name


class Journal (models.Model):
    #user = models.ForeignKey(User, related_name='User', null=True, on_delete=models.CASCADE)
    account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    Journal_name = models.CharField(max_length=300, unique=True)
    Journal_number = models.PositiveIntegerField(unique=True)
    Journal_description = models.TextField(null=True, blank=True)
    initial_journal_balance = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(0)])
    journal_debit = models.DecimalField(decimal_places=2, max_digits=10)
    journal_credit = models.DecimalField(decimal_places=2, max_digits=10)
    journal_balance = models.DecimalField(decimal_places=2, max_digits=10)
    source_document = models.FileField(upload_to='source_docs', null=True, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.Journal_name

