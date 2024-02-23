from django.db import models

# Create your models here.

class UserModel(models.Model):
    firstName = models.TextField(null=True)
    lastName = models.TextField(blank=True)
    email = models.EmailField(null=True)
    phoneNumber = models.PositiveIntegerField(null=True)
    education = models.TextField(null=True)
    skills = models.TextField(null=True)
    experience = models.TextField(null=True)
    profile = models.FileField(upload_to='uploads', null=True)