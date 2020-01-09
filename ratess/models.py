from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(max_length = 500)
    image_pic = models.ImageField(upload_to = 'images/')
    posted = DateTimeField()
