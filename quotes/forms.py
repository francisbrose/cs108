
from django import forms
from .models import Quote, Image

class CreateQuoteForm(forms.ModelForm):
    '''Form to add new quotes to the database'''
    class Meta:
        model = Quote
        fields = ['person', 'text', ]

# class UpdateQuoteForm(forms.ModelForm):
#     '''A form to update a database quote'''
#     class Meta:
#         model = Quote
#         fields = ['person', 'text', ]

# class AddImageForm(forms.ModelForm):
#     '''Form to collect an image from the user.'''
#     class Meta:
#         model = Image
#         fields - ["image_file",]