from django.forms import ModelForm
from django import forms

from .models import *

class BillForm(ModelForm):
    class Meta:
        model=Bill
        fields='__all__'


class CustomerContactForm(ModelForm):
    class Meta:
        model=CustomerContact
        fields='__all__'

# class UserContactForm(ModelForm):
#     class Meta:
#         model=UserContact
#         fields='__all__'

