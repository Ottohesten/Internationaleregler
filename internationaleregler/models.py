from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.




class RacismPoint(models.Model):
    description = models.CharField(max_length=200, help_text="Hvad sagde/gjorde personen")
    points = models.IntegerField(help_text="Hvor mange point får personen. Sæt minus foran hvis du vil give negative point")
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Hvem sagde/gjorde det")
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.description} - {self.points}"
    

