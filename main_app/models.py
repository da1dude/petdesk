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
    
    # def get_absolute_url(self):
    #     return reverse('toy_detail', kwargs={'pk': self.id})

class Pet(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    species = models.CharField(
        max_length=100,
        choices=SPECIES_CHOICES,
        default=SPECIES_CHOICES[0][0],
    )
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    rxs = models.ManyToManyField(Rx)
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
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_room_display()} on {self.date} for {self.pet}"

    
    # change the default sort
    class Meta:
        ordering = ['-date']

