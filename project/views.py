from django.shortcuts import render
from django.views.generic import *
from .models import *

# Create your views here.

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
#     def get_context_data(self,**kwargs):
#         '''Gets context dictionary to be used in template'''
#         context=super(DeleteStatusMessagePageView, self).get_context_data(**kargs)
#         message=StatusMessage.objects.get(pk=self.kwargs['status_pk'])
#         context['message']=message
#         return context
#     def get_success_url(self):
#         '''Gets URL to reroute to after deletion'''
#         pk=self.kwargs.get('pk')
#         message=StatusMessage.objects.filter(pk=pk).first()
#         return reverse('profile', kwargs={'pk':profile_pk})

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
    template_name='project/success.html'
    queryset=Specimen.objects.all()
    def get_object(self):
        '''Gets status to be deleted.'''
        status_pk=self.kwargs['message.pk']
        profile_pk=self.kwargs['profile.pk']
        message=StatusMessage.objects.get(pk=status_pk)
        return message
    def get_context_data(self,**kwargs):
        '''Gets context dictionary to be used in template'''
        context=super(DeleteStatusMessagePageView, self).get_context_data(**kargs)
        message=StatusMessage.objects.get(pk=self.kwargs['status_pk'])
        context['message']=message
        return context
    def get_success_url(self):
        '''Gets URL to reroute to after deletion'''
        pk=self.kwargs.get('pk')
        message=StatusMessage.objects.filter(pk=pk).first()
        return reverse('home')

class SuccessView(ListView):
    '''Displays page aftrer successful checkout.'''
    model = Check
    template_name = 'project/success.html'
    context_object_name = 'success'

class CreateIndividualView(CreateView):
    model=Individual
    template_name='project/checkout.html'
    context_object_name='individual'

def createindividualview(request): 
    '''Creates a new individual'''
    context ={} 
    form = IndividualForm(request.POST or None) 
    if form.is_valid(): 
        form.save() 
    context['form']= form 
    return render(request, "checkout.html", context) 

def CheckoutView(request,pk):
    template_name='project/checkout.html'
    context_object_name='checkout'
    form=CheckoutForm(request.POST or None, instance=pk)
    pk=get_object_or_404(Check,pk=pk)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/success')
    context["form"]=form
    return render(request, 'checkout.html', context)