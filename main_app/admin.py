from django.contrib import admin
# import your models here
from .models import Pet, Checkin

# Register your models here
admin.site.register(Pet)
admin.site.register(Checkin)
