from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Challenge(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    coordinator = models.ForeignKey(User)
    description = models.TextField()

class UserType(models.Model):
    GROUP_CHOICES = (
        ('ADMIN', 'Administrator'),
        ('COORDI', 'Coordinator'),
        ('MEMBER', 'Member'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.CharField(
        max_length=6,
        choices=GROUP_CHOICES,
        default='MEMBER',
    )