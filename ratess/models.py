from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 100)
    image = ImageField(blank=True, manual_crop="")
    description = models.TextField(max_length = 500)
    posted = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.name} Caption'

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()


class Profile(models.Model):
    bio = models.TextField(max_length = 500)
    profile_pic = ImageField(blank=True, manual_crop="")
    location = models.CharField(max_length = 100) 
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()
    
