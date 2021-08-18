from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request -> response
# this is request handler

def say_hello(request):
    #transfer data #send emails
    return render(request,'hello.html',{'name':'Json'})
