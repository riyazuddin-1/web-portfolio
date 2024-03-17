from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.greetings, name='greetings'),
    path('about/', views.aboutMe, name='about'),
    path('contact/', views.contactMe, name='contact')
]