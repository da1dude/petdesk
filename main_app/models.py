from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

# SPECIES = (
#     ('B', 'Bird'),
#     ('C', 'Cat'),
#     ('D', 'Dog')
# )

class Pet(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    #species = models.CharField(max_length=100)
    SPECIES_CHOICES = [
        ("B", "Bird"),
        ("C", "Cat"),
        ("D", "Dog"),
    ]
    species = models.CharField(
        max_length=100,
        choices=SPECIES_CHOICES,
        default=SPECIES_CHOICES[0][0],
    )
    # the reson it wasnt working bc we had an existing pet and we had more the 1 character and the max length was at 1 so switched it to 100 max length and it worked.

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
    
