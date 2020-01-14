from django.test import TestCase
from .models import Project, Profile
from django.contrib.auth.models import User

# Create your tests here.
class TestProject(TestCase):
    def setUp(self):
        
