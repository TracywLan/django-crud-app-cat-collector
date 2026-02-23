from django.db import models
from django.urls import reverse

# Create your models here.

class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
    # Define a method to get the URL for this particular cat instance
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this cat's details
        return reverse("cat-detail", kwargs={"cat_id": self.id})

# Why use reverse?
# Using reverse is better than hardcoding f"/cats/{self.id}". If you ever decide to change your URL path from /cats/ to /mycats/ in urls.py, reverse will update every link in your entire app automatically.


# Add new Feeding model below Cat model

class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(max_length=1)
