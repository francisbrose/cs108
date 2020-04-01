
from django import forms
from .models import Quote

class CreateQuoteForm(forms.ModelForm):
    '''Form to add new quotes to the database'''
    class Meta:
        model = Quote
        fields = ['person', 'text', ]

class UpdateQuoteForm(forms.ModelForm):
    '''A form to update a database quote'''
    class Meta:
        model = Quote
        fields = ['person', 'text', ]