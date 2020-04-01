from django.shortcuts import render

# Create your views here.

from .models import Quote
from django.views.generic import ListView, DetailView

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