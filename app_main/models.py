from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    level = models.IntegerField(blank=True, default=0)
    points = models.FloatField(blank=True, default=0)





    
