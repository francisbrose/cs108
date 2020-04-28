from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('check', CheckView.as_view(), name='check'),
    path('about', AboutView.as_view(), name='about'),
    path('all_specimens', AllSpecimensView.as_view(), name='all_specimens'),
    path('specimen/<int:pk>', SpecimenView.as_view(), name='specimen'),
    path('success', SuccessView.as_view(),name='success'),
    path('checkout/<int:pk>', CheckoutView, name='checkout'),
    path('checkout/<int:pk>/delete', DeleteCheckView.as_view(), name='delete'),
    path('user', CreateIndividualView, name='user'),

]