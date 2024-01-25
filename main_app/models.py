from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

SPECIES_CHOICES = [
    ("B", "Bird"),
    ("C", "Cat"),
    ("D", "Dog"),
    ("F", "Ferret"),
    ("H", "Hamster"),
    ("G", "Guinea Pig"),
    ("L", "Lizard"),
    ("R", "Rabbit"),
]

ROOM_CHOICES = [
    ("1", "Room 1"),
    ("2", "Room 2"),
    ("3", "Room 3"),
    ("4", "Room 4"),
    ("5", "Room 5"),
]





class Rx(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    treatment = models.TextField(max_length=250)

    def __str__(self):
        return f'{self.name} - {self.description} - {self.treatment}'
    
    def get_absolute_url(self):
        return reverse('rxs_detail', kwargs={'pk': self.id})

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(
        max_length=100,
        choices=SPECIES_CHOICES,
        default=SPECIES_CHOICES[0][0],
    )
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
    

class Checkin(models.Model):
    date = models.DateField('checkin date')
    room = models.CharField(
        max_length=100,
        choices=ROOM_CHOICES,
        default=ROOM_CHOICES[0][0],
    )
    reason = models.TextField(max_length=250)
    notes = models.TextField(max_length=250, null = True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    rxs = models.ManyToManyField(Rx)

    def __str__(self):
        return f"{self.get_room_display()} on {self.date} for {self.pet}"
    
    def get_absolute_url(self):
        return reverse('checkin_detail', kwargs={'checkin_id': self.id})    

    
    # change the default sort
    class Meta:
        ordering = ['-date']


class Photo(models.Model):
    url = models.CharField(max_length=200)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for pet_id: {self.pet_id} @{self.url}"