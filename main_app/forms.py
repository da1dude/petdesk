from django.forms import ModelForm
from .models import Checkin

class CheckinForm(ModelForm):
    class Meta:
        model = Checkin
        fields = ['date', 'room', 'reason']