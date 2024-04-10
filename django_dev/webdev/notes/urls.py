from django.urls import path

from . import views

urlpath = [
    path("index.html" , views.index, name="index")
]