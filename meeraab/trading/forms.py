from .models import *
from django.forms import ModelForm
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class TradeForm(ModelForm):
    class Meta:
        model = Trade
        exclude = ['creator','slug',]
        widgets = {
            'publish':DateInput(),
            'expire':DateInput(),
        }
