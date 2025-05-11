from django.db import models

# Create your models here.

# we define our data entities, blueprints for dataobjects , we are going to work with

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()