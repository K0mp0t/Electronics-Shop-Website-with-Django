from django import forms
from .models import *

class CheckOrderForm(forms.Form):
    nmb = forms.IntegerField(required=True)