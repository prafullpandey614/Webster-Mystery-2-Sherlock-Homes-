from distutils.command.upload import upload
from email.policy import default
from hashlib import blake2b
from statistics import mode
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Group, Permission


class Degree(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return f"{self.name}"
    
class Skill(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return f"{self.name} "
    
class Jobs(models.Model):
    title = models.CharField(max_length=40)
    required_qualifications = models.ManyToManyField(Degree)
    skills = models.ManyToManyField(Skill)
    last_date = models.DateField()
    def __str__(self):
        return f"{self.title} {self.last_date}"


def default_image_path():
    return 'media/th_19.jfif'  
class User(AbstractUser):
    name = models.CharField(max_length=20,blank=True,null=True)
    dp = models.ImageField(upload_to="media",default = default_image_path)
    dob = models.DateField(blank=True,null=True)
    jobs_applied = models.ManyToManyField(Jobs,null=True,blank=True)
    highest_qualification = models.ForeignKey(Degree,blank=True,on_delete=models.CASCADE,null=True)
    contact = models.CharField(max_length=10,null=True,blank=True)
    resume = models.FileField(upload_to='media',blank=True,null=True)

