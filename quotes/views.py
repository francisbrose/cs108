from django.shortcuts import render

# Create your views here.

from .models import Quote, Person
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .forms import CreateQuoteForm, UpdateQuoteForm
import random

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
        q = all_quotes(r)
        return q

class PersonPageView(DetailView):
    '''Shows all quotes and images for one person'''

    model = Person
    template_name = 'quotes/person.html'
    context_object_name = 'person'

class CreateQuoteView(CreateView):
    '''View to create a new quote and save it to the database'''
    form_class = CreateQuoteForm
    template_name = "quotes/create_quote.html"

class UpdateQuoteView(UpdateView):
    '''View to update a quote and save it to the database'''
    form_class = UpdateQuoteForm
    template_name = "quotes/update_quote.html"
    queryset = Quote.objects.all()
