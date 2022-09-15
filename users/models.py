from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from internationaleregler.models import RacismPoint

# Create your models here.


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    

    
    def __str__(self):
        return f"{self.user}"
    
