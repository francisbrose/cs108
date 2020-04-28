from django import forms
from .models import *

class CheckoutForm(forms.ModelForm):
    '''Form to checkout specimens in the database.'''
    context_object_name='checkout_form'
    class Meta:
        fields = ['Specimen', 'Individual', 'Checkin', 'Checkout']

class IndividualForm(forms.ModelForm):
    '''Form to add new individual to the database.'''
    context_object_name='individual_form'
    class Meta:
        fields = ['Name', 'Email', 'Department']