from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 100)
    image = ImageField(blank=True, manual_crop="")
    description = models.TextField(max_length = 500)
    posted = models.DateTimeField(auto_now_add=True, null=True)
    

class Profile(models.Model):
    bio = models.TextField(max_length = 500)
    profile_pic = ImageField(blank=True, manual_crop="")
    location = models.CharField(max_length = 100) 