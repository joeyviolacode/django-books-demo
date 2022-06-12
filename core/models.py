from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField

class User(AbstractUser):
    pass

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=63)
    year = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=5000, null=True, blank=True)

# class Author(models.Model):
#     name = models.CharField(max_length=255)
#     books = 