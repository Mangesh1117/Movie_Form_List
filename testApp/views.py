from django.shortcuts import render
from . import models
from . import forms

def index_view(request):
    dictObj = {"name":"Rahul"}
    return render(request,"testApp/index.html",dictObj)

def add_view(request):
    dictObj = {'submit':False}
    fobj = forms.MovieForm()
    if(request.method == "POST"):
        fobj = forms.MovieForm(request.POST)
        if(fobj.is_valid()):
            fobj.save(commit=True)
            print("Validation Successfull")
            dictObj['submit'] = True
    dictObj['form'] = fobj
    fobj = forms.MovieForm()

    return render(request,"testApp/addMovie.html",dictObj)

def list_view(request):
    movie_list = models.Movie.objects.all()
    dictObj = {'list':movie_list}
    return render(request,"testApp/listMovie.html",dictObj)