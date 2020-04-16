from django.db import models

class Specimens(models.Model):
    '''Models all specimens currently available in the inventory.'''
    name=models.TextField(blank=False)
    catagory=models.TextField(blank=False)
    image=models.URLField(blank=False)

class Check(models.Model):
    '''Models a record of specimens taken out.'''
    specimen=models.TextField(blank=False)
    checkout=models.DateTimeField(auto_now_add=True)
    checkin=models.DateTimeField(auto_now_add=True)

class Individuals(models.Model):
    '''Models individuals registered in system to check out.'''
    name=models.TextField(blank=False)
    email=models.TextField(blank=False)
    department=models.TextField(blank=True)
    lab=models.TextField(blank=True)