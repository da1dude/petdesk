from django.shortcuts import render
from .models import Pet

# Create your views here.

# Define the home view
def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')

def about(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'about.html')

def pets_index(request):
    #collect our objects from the db
    # cats = Cat.objects.all()
    pets = Pet.objects.filter(user=request.user)
    # You could also retrieve the logged in user's cats like this
    # cats = request.user.cat_set.all()
    return render(request, 'pets/index.html', { 'pets': pets })

def pets_detail(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    return render(request, 'pets/detail.html', { 'pet': pet })

