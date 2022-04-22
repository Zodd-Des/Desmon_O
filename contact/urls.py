from django.urls import path
from . import views

urlpatterns = [
    # path to acces the home page
    path('',views.index, name='index'),
    # path to send the form to the backend
    path('contact', views.contact, name='contact')
]