from django import forms
from .models import *

class CheckoutContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    comments = forms.CharField(widget=forms.Textarea)