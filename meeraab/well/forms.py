from .models import *
from django.forms import ModelForm
from django import forms


class WellForm(ModelForm):
    class Meta:
        model = Well
        fields = ['owner', 'name', 'license', 'licensePic', 'permitedAbdehi', 'permitedWorkTime', 'UTM', 'useType', 'permitedUseInYear', 'chargeInYear',]


class WellPhysicalInfoForm(ModelForm):
    class Meta:
        model = WellPhysicalInfo
        fields =['farmingType', 'area', 'depth', 'power', 'abdehi', 'pomp', 'buyCap', 'sellCap', 'wellCap',]

class BeneficiaryForm(ModelForm):
    class Meta:
        model = Beneficiary
        fields =['firstname', 'lastname', 'idNumber', 'phoneNumber',]
