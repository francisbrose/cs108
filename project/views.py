from django.shortcuts import render
from django.views.generic import *
from .models import *
from .forms import *

class HomeView(ListView):
    '''Shows home page.'''
    model = Specimen
    template_name = 'project/home.html'
    context_object_name = 'home'

class CheckView(ListView):
    '''Displays checkout page.'''
    model=Check
    template_name='project/check.html'
    queryset=Specimen.objects.all()
    success_url='/'

class AllSpecimensView(ListView):
    '''Displays all specimens.'''
    model = Specimen
    template_name = 'project/all_specimens.html'
    context_object_name = 'all_specimens'

class AboutView(ListView):
    '''Displays about page.'''
    model = Specimen
    template_name = 'project/about.html'
    context_object_name = 'about'

class SpecimenView(DetailView):
    '''Displays one specimen's page.'''
    model = Specimen
    template_name = 'project/specimen.html'
    context_object_name = 'specimen'

class DeleteCheckView(DeleteView):
    '''Deletes a reservation.'''
    template_name='project/delete.html'
    model = Check 
    success_url='/'



class SuccessView(ListView):
    '''Displays page aftrer successful checkout.'''
    model = Check
    template_name = 'project/success.html'
    context_object_name = 'check_list'
    def get_queryset(self):
        return Check.objects.all()

def CreateIndividualView(request): 
    '''Creates a new individual'''
    form = IndividualForm(request.POST or None) 
    if form.is_valid(): 
        form.save() 
    return render(request, "project/user.html", {'form': form}) 

def CheckoutView(request,pk):
    form=CheckoutForm(request.POST)
    if form.is_valid():
        form.save()
    #context["form"]=form
    return render(request, "project/checkout.html", {'form': form})