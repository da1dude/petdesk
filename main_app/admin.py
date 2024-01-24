from django.contrib import admin
# import your models here
from .models import Pet, Checkin, Rx, Photo

# Register your models here
admin.site.register(Pet)
admin.site.register(Checkin)
admin.site.register(Rx)
admin.site.register(Photo)
