from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request): # This is the view function
    return render(request, 'notes/index.html') # This is the view template
