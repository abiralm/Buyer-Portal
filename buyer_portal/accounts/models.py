from django.contrib.auth.models import AbstractUser
from django.db import models


#user model
class User(AbstractUser):
    ROLE_CHOICES = [('buyer', 'Buyer'), ('agent', 'Agent')]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='buyer')
    
    def __str__(self):
        return self.email