from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(max_length = 500)
    image_pic = models.ImageField(upload_to = 'images/')
    posted = models.DateTimeField(auto_now_add=True, null=True)

class Profile(models.Model):
    bio = models.TextField(max_length = 500)
    Profile_pic = models.ImageField(upload_to = 'profile_images/')
    location = models.CharField(max_length = 100) 
