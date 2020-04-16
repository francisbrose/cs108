from django.shortcuts import render

# Create your views here.

class HomeView(ListView):
    '''Shows home page.'''
    model = Checkout
    template_name = 'final/home.html'
    context_object_name = 'home'

class CheckView(Detail)



class DeleteStatusMessageView(DetailView):
    '''Displays checkout page.'''
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
