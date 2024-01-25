from django.forms import ModelForm
from .models import Checkin, Rx

class CheckinForm(ModelForm):
    class Meta:
        model = Checkin
        fields = ['date', 'room', 'reason']

