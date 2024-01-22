from django.forms import ModelForm
from .models import Checkin, Rx

class CheckinForm(ModelForm):
    class Meta:
        model = Checkin
        fields = ['date', 'room', 'reason']

class RxForm(ModelForm):
    class Meta:
        model = Rx
        fields = ['name', 'description', 'treatment']