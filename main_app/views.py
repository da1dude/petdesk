import uuid
import boto3
import os
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pet, Rx, Checkin, Photo



from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Import the login_required decorator
from django.contrib.auth.decorators import login_required
# Import the mixin for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CheckinForm

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
    # You could also retrieve the logged in user's pets like this
    # pets = request.user.pet_set.all()
    return render(request, 'pets/index.html', { 'pets': pets })


@login_required
def pets_detail(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    checkin_form = CheckinForm()  
    return render(request, 'pets/detail.html', { 
        'pet': pet,
        'checkin_form': checkin_form, 
    })


class PetCreate(LoginRequiredMixin, CreateView):
    model = Pet
    # this view creates a form, so we need to identify which fields to use
    fields = ['name', 'species', 'description', 'age', 'comment']
    # This inherited method is called when a
    # valid pet form is being submitted
    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  
        return super().form_valid(form)

# Update Pet
class PetUpdate(LoginRequiredMixin, UpdateView):
    model = Pet
    fields = ['description', 'age', 'comment']


class PetDelete(LoginRequiredMixin, DeleteView):
    model = Pet
    success_url = '/pets'


class RxCreate(LoginRequiredMixin, CreateView):
    model = Rx
    # this view creates a form, so we need to identify which fields to use
    fields = ['name', 'description', 'treatment']
    # This inherited method is called when a
    # valid pet form is being submitted
    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  
        return super().form_valid(form)

class RxList(LoginRequiredMixin, ListView):
    model = Rx
    template_name = 'rxs/index.html'

class RxDetail(LoginRequiredMixin, DetailView):
    model = Rx
    template_name = 'rxs/detail.html'

class RxDelete(LoginRequiredMixin, DeleteView):
    model = Rx
    success_url = '/rxs'

class RxUpdate(LoginRequiredMixin, UpdateView):
    model = Rx
    fields = ['name', 'description', 'treatment']


@login_required
def checkin_detail(request, checkin_id):
    checkin = Checkin.objects.get(id=checkin_id)
    id_list = checkin.rxs.all().values_list('id')
    rxs_checkin_doesnt_have = Rx.objects.exclude(id__in=id_list)
    checkin_form = CheckinForm()  
    return render(request, 'checkins/detail.html', { 
        'checkin': checkin,
        'checkin_form': checkin_form, 
        'rxs': rxs_checkin_doesnt_have
    })

class CheckinUpdate(LoginRequiredMixin, UpdateView):
    model = Checkin
    fields = ['reason', 'notes']

@login_required
def assoc_rx(request, checkin_id, rx_id):
    # Note that you can pass a rx's id instead of the whole rx object
    Checkin.objects.get(id=checkin_id).rxs.add(rx_id)
    return redirect('checkin_detail', checkin_id=checkin_id)

@login_required
def unassoc_rx(request, checkin_id, rx_id):
    # Note that you can pass a rx's id instead of the whole rx object
    Checkin.objects.get(id=checkin_id).rxs.remove(rx_id)
    return redirect('checkin_detail', checkin_id=checkin_id)


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

@login_required
def add_photo(request, pet_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # we can assign to pet_id or pet (if you have a pet object)
            Photo.objects.create(url=url, pet_id=pet_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', pet_id=pet_id)


@login_required
def add_checkin(request, pet_id):
    form = CheckinForm(request.POST)
    if form.is_valid():
        new_checkin = form.save(commit=False)
        new_checkin.pet_id = pet_id
        new_checkin.save()
    return redirect('detail', pet_id=pet_id)

