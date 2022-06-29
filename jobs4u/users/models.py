from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to='profile_pics')
    address = models.CharField(max_length=255, blank=False)
    IsCurrentlyEmployed = models.BooleanField(default=False)
    birth_year = models.DateTimeField()


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField()
    image = models.ImageField()

