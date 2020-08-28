from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    display_name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.display_name
