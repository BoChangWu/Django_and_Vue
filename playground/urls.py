# map urls to view functions
from django.urls import path
from . import views

# URLConfiguration
#this is a special variable that django looks for
urlpatterns= [
    path('hello/',views.say_hello) #returns urlpattern object
]