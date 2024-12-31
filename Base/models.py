from django.db import models
from django.forms import DateTimeField

class About(models.Model):
    story = models.TextField()
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    image = models.ImageField(upload_to='About/')

class Skill(models.Model):
    name = models.CharField(max_length=30)
    level = models.PositiveIntegerField()  # Restrict to non-negative integers
    image = models.ImageField(upload_to='Skill/')

class Education(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to='Education/')

class Project(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Project/')
    description = models.TextField()
    link = models.URLField(max_length=200)  # Use URLField for validation

class Message(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True)