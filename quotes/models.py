from django.db import models
from django.urls import reverse
import random
# Create your models here.

class Person(models.Model):
    '''Encapsulate theconcept of a person who said a famous quote'''
    name=models.TextField(blank=False)
    def __str__(self):
        '''Returns str of this person'''
        return self.name
    def get_random_image(self):
        '''Return random image of this person'''
        images = Image.objects.filter(person=self.pk)
        i - random.randint(0, len(images) -1)
        return images(i)
    def get_all_images(self):
        '''returns all images of a person'''
        images = Image.objects.filter(person=self.pk)
        return images
    def get_all_quotes(self):
        '''returns all quotes of a person'''
        quotes = Quote.objects.filter(person=self.pk)
        return quotes    

class Quote(models.Model):
    '''Encapsulaye the idea of a quote'''
    #data attributes of a quote
    text = models.TextField(blank=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)

    def __str__(self):
        '''Return a string representation of this object.'''
        return '"%s" - %s' % (self.text, self.person.name)
    
    def get_absolute_url(self):
        '''Return a url to display quote'''
        return reverse("quote", kwargs={"pk:self.pk"})


class Image(models.Model):
    '''Represent an image associated with a person.'''
    image_url = models.URLField(blank=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    def __str__(self):
        '''Return a string representation of this image.'''
        return self.image_url


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