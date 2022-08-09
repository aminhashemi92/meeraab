from .models import *
from django.forms import ModelForm
from django import forms


class ChargeAndCreditForm(ModelForm):
    class Meta:
        model = ChargeAndCredit
        fields = ['annual_charge', 'used_charge', 'remaining_charge', 'detail', 'status',]


class TechnicalConditionForm(ModelForm):
    class Meta:
        model = TechnicalCondition
        fields =['operation_license', 'calibrated', 'document', 'detail', 'status',]


class ModifyNameForm(ModelForm):
    class Meta:
        model = ModifyName
        fields =['document', 'license', 'detail', 'status',]


class CommitmentForm(ModelForm):
    class Meta:
        model = Commitment
        fields =['document', 'detail', 'status',]


class IssuanceForm(ModelForm):
    class Meta:
        model = Issuance
        fields =['annual_charge', 'used_charge', 'remaining_charge', 'detail', 'status',]
