from .models import *
from django.forms import ModelForm
from django import forms


class ChahvandToAbvandTransactionForm(ModelForm):
    type = forms.CharField(widget=forms.HiddenInput(), initial='ca')
    class Meta:
        model = Transaction
        exclude = ['from_abvand','to_chahvand','from_well','to_well',]


class AbvandToAbvandTransactionForm(ModelForm):
    type = forms.CharField(widget=forms.HiddenInput(), initial='aa')
    class Meta:
        model = Transaction
        exclude = ['from_chahvand','to_chahvand','from_well','to_well',]


class AbvandToChahvandTransactionForm(ModelForm):
    type = forms.CharField(widget=forms.HiddenInput(), initial='ac')
    class Meta:
        model = Transaction
        exclude = ['to_abvand','from_chahvand','from_well','to_well',]


class ChahToChahvandTransactionForm(ModelForm):
    type = forms.CharField(widget=forms.HiddenInput(), initial='wc')
    class Meta:
        model = Transaction
        exclude = ['to_abvand','from_chahvand','to_well','from_abvand','bucket']


class ChahvandToChahTransactionForm(ModelForm):
    type = forms.CharField(widget=forms.HiddenInput(), initial='cw')
    class Meta:
        model = Transaction
        exclude = ['to_abvand','to_chahvand','from_well','from_abvand',]



    # def __init__(self, *args, **kwargs):
    #     super(CreateUserForm, self).__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'input1'
