from django.db import models
from django import forms
from .forms import *

class Specimen(models.Model):
    '''Models all specimens currently available in the inventory.'''
    c_name=models.TextField(blank=False)
    category=models.TextField(blank=False)
    image=models.TextField(blank=False)
    kingdom=models.TextField(blank=False)
    phylum=models.TextField(blank=False)
    classs=models.TextField(blank=False)
    order=models.TextField(blank=False)
    family=models.TextField(blank=False)
    genus=models.TextField(blank=False)
    species=models.TextField(blank=False)
    s_species=models.TextField(blank=True)

class Check(models.Model):
    '''Models a record of specimens taken out.'''
    checkout=models.DateField(auto_now_add=True,null=False)
    checkin=models.DateField(auto_now_add=True,null=False)

class Individual(models.Model):
    '''Models individuals registered in system to check out.'''
    name=models.TextField(blank=False,null=False)
    email=models.TextField(blank=False,null=False)
    department=models.TextField(blank=True,null=False)