from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('quote/', views.quote, name='quote'),
    path('quote/success/', views.quote_success, name='quote_success'),
    path('samples/', views.samples, name='samples'),
    path('reviews/', views.reviews, name='reviews'),
    path('contact/', views.contact, name='contact'),
]