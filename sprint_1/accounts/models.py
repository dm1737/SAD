from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords



# Create your models here.
from django.db import models

class UserAccount (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=300, unique=True)
    account_number = models.IntegerField(unique=True)
    account_description = models.TextField()
    #normal_side = models.TextField() 
    account_category = models.CharField(max_length=300)
    account_subcategory = models.CharField(max_length=300)
    initial_balance = models.DecimalField(decimal_places=2, max_digits=10)
    debit = models.DecimalField(decimal_places=2, max_digits=10)
    credit = models.DecimalField(decimal_places=2, max_digits=10)
    balance = models.DecimalField(decimal_places=2, max_digits=10)
    account_created = models.DateTimeField(default=datetime.now)
    order = models.CharField(max_length=300)
    statement = models.FileField(null=True)
    comment = models.TextField()
    history = HistoricalRecords()


    def __str__(self):
        return self.user.username

class Post(models.Model):
    username= models.CharField(max_length=300, unique=True)
    password= models.TextField()
