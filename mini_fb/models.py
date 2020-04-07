from django.db import models

# Create your models here.

class Profile(models.Model):
    '''Models the data attributes of Facebook users'''
    name=models.TextField(blank=False)
    def f_name(self):
        '''Returns first name'''
        return self.f_name

    def l_name(self):
        '''Returns last name'''
        return self.l_name

    def city(self):
        '''Returns person's city'''
        return self.city

    def email(self):
        '''Returns person's email'''
        return self.email

    def image(self):
        '''Returns image of person'''
        image = Image.objects.filter(person=self.pk)
        return image
        
    def __str__(self):
        '''Return a string representation of this profile.'''
        return self.Profile