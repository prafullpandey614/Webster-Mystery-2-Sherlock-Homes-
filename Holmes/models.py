from hashlib import blake2b
from statistics import mode
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Group, Permission


class Degree(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return f"{self.name}"

class Jobs(models.Model):
    title = models.CharField(max_length=40)
    required_qualifications = models.OneToOneField(Degree,on_delete=models.CASCADE)
    skills = models.TextField(blank=True)
    last_date = models.DateField()
    def __str__(self):
        return f"{self.title} {self.last_date}"


class User(AbstractUser):
    name = models.CharField(max_length=20,blank=True,null=True)
    dp = models.ImageField(upload_to="media",blank=True,null=True)
    dob = models.DateField(blank=True,null=True)
    jobs_applied = models.ForeignKey(Jobs,on_delete=models.CASCADE,null=True,blank=True)
    highest_qualification = models.ForeignKey(Degree,blank=True,on_delete=models.CASCADE,null=True)
    contact = models.CharField(max_length=10,null=True,blank=True)

