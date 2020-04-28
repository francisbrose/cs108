from django import forms
from .models import *

class CheckoutForm(forms.ModelForm):
    '''Form to checkout specimens in the database.'''
    context_object_name='checkout_form'
    class Meta:
        model=Check
        fields = ['specimen', 'individual', 'checkin', 'checkout']

class IndividualForm(forms.ModelForm):
    '''Form to add new individual to the database.'''
    context_object_name='individual_form'
    class Meta:
        model=Individual
        fields = ['name', 'email', 'department']