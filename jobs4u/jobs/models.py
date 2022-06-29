from tkinter import CASCADE
from django.db import models
from users.models import Person, Employer
# Create your models here.


class Job(models.Model):
    employer = models.OneToOneField(Employer, blank=True, on_delete=models.CASCADE())
    requirements = models.TextField(blank=False)
    isFree = models.BooleanField(default=True)
    title = models.CharField(max_length=50, blank=False)




