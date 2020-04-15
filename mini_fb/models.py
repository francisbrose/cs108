from django.db import models
from django import forms

class Profile(models.Model):
    '''Models the data attributes of Facebook users'''
    l_name=models.TextField(blank=False)
    f_name=models.TextField(blank=False)
    name = "%s %s" % (f_name, l_name)
    email = models.TextField(blank=True)
    city=models.TextField(blank=True)
    image = models.URLField(blank=True)
    bday=models.TextField(blank=True)
    friends = models.ManyToManyField("self")
    def __str__(self):
        '''Return a string representation of this profile.'''
        return '%s %s' %(self.f_name,self.l_name)
    
    def get_absolute_url(self):
        '''Gets URL for single profile'''
        return reverse('profile', kwargs={'pk':self.pk})

    def get_status_messages(self):
        '''Obtains status messages for profile'''
        message=StatusMessage.objects.filter(profile=self.pk)
        return message
    
    def get_friend_suggestions(self):
        '''Gets possible friends for profile'''
        possible_friends = Profile.objects.all().exlude(pk__in=self.get_friends()).exclude(pk=self.pk)
        return possible_friends

    def get_news_feed(self):
        '''Gets news feed for profile'''
        news = StatusMessage.objects.all().order_by("-timestamp")
        return news

    def get_friends(self):
        '''Gets friends of this profile'''
        Queryset=self.friends.all().exclude(pk=self.pk)
        return Queryset


class StatusMessage(models.Model):
    '''Models a status message by users'''
    timestamp=models.DateTimeField(auto_now_add=True)
    message=models.TextField(blank=False)
    image=models.ImageField(blank=True)
    profile=models.ForeignKey("Profile", on_delete=models.CASCADE, blank=False)
    def __str__(self):
        '''Return a string representation of this status message.'''
        return '%s: %s (Posted at %s)' %(self.profile, self.message, self.timestamp)