from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

SPECIES = (
    ('B', 'Bird'),
    ('C', 'Cat'),
    ('D', 'Dog')
)

class Pet(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    comment = models.TextField(max_length=250)
    # Add the foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    # this is the get_absolute_url method, it redirects to the detail page where approprite
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pet_id': self.id})