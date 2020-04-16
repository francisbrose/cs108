from django import forms
from .models import *

class CheckoutForm(forms.ModelForm):
    '''Form to add new status messages to the database.'''
    message=forms.CharField(label="Message", required=True)
    image=forms.ImageField(label='Image', required=False)
    context_object_name='checkout_form'
    class Meta:
        model = StatusMessage
        fields = ['message', 'image']