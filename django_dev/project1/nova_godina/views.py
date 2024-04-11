import datetime
from django.shortcuts import render

# Create your views here.

def index(request):
    sad = datetime.datetime.now()
    return render(request, 'nova_godina/index.html'),{
        "nova_godina": sad.month == 1 and sad.day == 1
    }
    