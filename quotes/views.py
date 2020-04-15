from django.shortcuts import render

# Create your views here.

from .models import Quote, Person
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from .forms import CreateQuoteForm
import random
from django.urls import reverse
from django.shortcuts import redirect

class HomePageView(ListView):
    '''Create subclass of ListView to display all quotes'''
    model = Quote
    template_name = 'quotes/home.html'
    context_object_name = 'all_quotes_list'

class QuotePageView(DetailView):
    '''Shows details for one quote.'''
    model = Quote
    template_name = 'quotes/quote.html'
    context_object_name = 'quote'

class RandomQuotePageView(DetailView):
    '''Shows a random quote'''
    model = Quote
    template_name = 'quotes/quote.html'
    context_object_name = 'quote'

    def get_object(self):
        '''Return a single quote object.'''
        all_quotes = Quote.objects.all()
        r= random.randint(0, len(all_quotes) -1)
        q = all_quotes[r]
        return q

class PersonPageView(DetailView):
    '''Shows all quotes and images for one person'''
    model = Person
    template_name = 'quotes/person.html'
    context_object_name = 'person'
    def get_context_data(self, **kwargs):
        '''Return a dict with context data for this template'''
        context = super(PersonPageView, self).get_context_data(**kwargs)
        add_image_form = AddImageForm()
        context['add_image_form'] = add_image_form
        return context

# class CreateQuoteView(CreateView):
#     '''View to create a new quote and save it to the database'''
#     form_class = CreateQuoteForm
#     template_name = "quotes/create_quote.html"

# class UpdateQuoteView(UpdateView):
#     '''View to update a quote and save it to the database'''
#     form_class = UpdateQuoteForm
#     template_name = "quotes/update_quote.html"
#     queryset = Quote.objects.all()

# class DeleteQuoteView(DeleteView):
#     '''View to delete a quote and save it to the database'''
#     template_name = "quotes/delete_quote.html"
#     queryset = Quote.objects.all()
#     #success_url="../../all"
#     def get_success_irl(self):
#         '''Return URL to be directed to after delete.'''
#         pk = self.kwargs.get('pk')
#         quote = Quote.objects.filter(pk=pk).first()
#         person = quote.Person
#         return reverse('person', kwargs={'pk':person.pk})

def add_image(request, pk):
    '''Custom view function to handle submission of an image upload.'''
    person = Person.objects.get(pk=pk)
    form = AddImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        sm = form.save(commit=False)
        sm.person = person
        sm.save()
    else:
        print("Error: the form was not valid.")
    url = reverse('person', kwargs={'pk':pk})
    return redirect(url)