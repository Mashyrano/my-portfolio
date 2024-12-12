from django.db import models

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
