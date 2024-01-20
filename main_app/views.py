from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pet

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Import the login_required decorator
from django.contrib.auth.decorators import login_required
# Import the mixin for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# Define the home view
def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')

def about(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'about.html')


@login_required
def pets_index(request):
    #collect our objects from the db
    pets = Pet.objects.filter(user=request.user)
    # You could also retrieve the logged in user's cats like this
    # cats = request.user.cat_set.all()
    return render(request, 'pets/index.html', { 'pets': pets })


@login_required
def pets_detail(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    return render(request, 'pets/detail.html', { 'pet': pet })


class PetCreate(LoginRequiredMixin, CreateView):
    model = Pet
    # this view creates a form, so we need to identify which fields to use
    fields = ['name', 'owner', 'species', 'description', 'age', 'comment']
    # This inherited method is called when a
    # valid pet form is being submitted
    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  
        return super().form_valid(form)


class PetUpdate(LoginRequiredMixin, UpdateView):
    model = Pet
    fields = ['owner', 'description', 'age', 'comment']


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class PetDelete(LoginRequiredMixin, DeleteView):
    model = Pet
    success_url = '/pets'
