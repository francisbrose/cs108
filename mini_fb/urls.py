# file: mini_fb/urls.py
# description: direct URL requests to view functions

from django.contrib import admin 
from django.urls import path, include 
from .views import *

urlpatterns = [
    path('', ShowAllProfilesView.as_view(), name='show_all_profiles'),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('create_profile', CreateProfileView.as_view(), name='create_profile'),
    path('profile/<int:pk>/post_status', create_status_message, name='post_status'),
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name='update_profile'),
    path('profile/<int:profile_pk>/news_feed', ShowNewsFeedView.as_view(), name='show_news_feed'),
    path('profile/<int:profile_pk>/delete_status/<int:status_pk>', DeleteStatusMessageView.as_view(), name='delete_status_message'),
    path('profile/<int:profile_pk>/add_friend/<int:friend_pk>', ShowPossibleFriendsView.as_view(), name='add_friend'),

]