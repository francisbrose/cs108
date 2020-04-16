from django.shortcuts import render
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import *
from .forms import CreateStatusMessageForm, CreateProfileForm, UpdateProfileForm

class ShowAllProfilesView(ListView):
    '''Shows all profiles.'''
    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'show_all_profiles'
    
class ShowProfilePageView(DetailView):
    '''Shows one profile.'''
    model = Profile
    template_name = 'mini_fb/show_profile_page.html'
    context_object_name = 'profile'
    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        form = CreateStatusMessageForm()
        context['create_status_form'] = form
        return context

class CreateProfileView(CreateView):
    '''Creates a new profile to save to the database.'''
    form_class = CreateProfileForm
    template_name = 'mini_fb/create_profile.html'
    context_object_name = 'create_profile_view'

def create_status_message(request, pk):
    '''Process a form submission to post a new status message.'''
    profile = Profile.objects.get(pk=pk)
    context_object_name="create_status_message"
    if request.method == 'POST':
        message = request.POST['message']
        image = request.FILES.get['image_file']
        form=CreateStatusMessageForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            sm=StatusMessage()
            sm.profile=profile
            sm.message=message
            image=form.save(commit=False)
            sm.save()
        else: print("Error: Invalid form.")
    return redirect(reverse('show_profile_page', kwargs={'pk': pk}))

class UpdateProfileView(UpdateView):
    '''Updates a profile to the database.'''
    form_class = UpdateProfileForm
    template_name = 'mini_fb/update_profile.html'
    context_object_name = 'update_profile'
    queryset=Profile.objects.all()

class ShowNewsFeedView(DetailView):
    '''Shows the news feed'''
    model = Profile
    template_name = 'mini_fb/show_news_feed.html'
    context_object_name='show_news_feed'
    queryset=Profile.objects.all()
    def get_object(self):
        '''Gets news feed objects to display.'''
        profile_pk=self.kwargs.get('profile_pk')
        newsfeed=Profile.objects.get(pk=profile_pk)
        return newsfeed

class DeleteStatusMessageView(DeleteView):
    '''Deletes a status message'''
    template_name='mini_fb/delete_status_form.html'
    queryset=Profile.objects.all()
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
        return reverse('profile', kwargs={'pk':profile_pk})

class ShowPossibleFriendsView(DetailView):
    '''Shows all possible friends for a given profile.'''
    model=Profile
    template_name = 'mini_fb/show_possible_friends.html'

def add_friend(request, profile_pk, friend_pk):
    '''Processes an add_friend request and adds friend to profile.'''
    requester=Profile.objects.get(pk=profile.pk)
    requestee=Profile.objects.get(pk=friend.pk)
    requester.friends.add(requestee)
    requester.save()
    return redirect(reverse('show_profile_page', kwargs={'pk':profile_pk}))
