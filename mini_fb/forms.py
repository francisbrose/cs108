from django import forms
from .models import Profile, StatusMessage

class CreateStatusMessageForm(forms.ModelForm):
    '''Form to add new status messages to the database.'''
    message=forms.CharField(label="Message", required=True)
    image=forms.ImageField(label='Image', required=False)
    context_object_name='status_form'
    class Meta:
        model = StatusMessage
        fields = ['message', 'image']

class UpdateProfileForm(forms.ModelForm):
    '''Form to update profile to database.'''
    class Meta:
        model = Profile
        fields = ['email','city','image']

class CreateProfileForm(forms.ModelForm):
    '''Form to create a profile to save to database.'''
    f_name = forms.CharField(label="First Name", required=True)
    l_name = forms.CharField(label="Last Name", required=True)
    email = forms.EmailField(label="Email", required=False)
    city = forms.CharField(label="City", required=False)
    image = forms.ImageField(label="Profile Image", required=False)
    bday = forms.DateField(label="Birthday", widget=forms.SelectDateWidget(years=range(2012,1920,-1),), required=False)
    class Meta:
        model = Profile
        fields = ['email','city','image','f_name','l_name','bday']
