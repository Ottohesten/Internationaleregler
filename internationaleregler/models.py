from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


MY_CHOICES = (
    ('OTTO', 'Otto'),
    ('NICOLAI', 'Nicolai'),
    ('SILAS', 'Silas'),
    ('BENJAMIN', 'Benjamin'),
    ('JOAKIM', 'Joakim'),
    ('JOHN', 'John'),
    ('IDA', 'Ida'),
)



class RacismPoint(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    points = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} - {self.points}"
    

