from django.http import HttpResponse
from django.shortcuts import render
from meetings.models import Meeting

# Create your views here.

def welcome(request):
    return render(request, "website/welcome.html",context={"meetings":Meeting.objects.all()})

def about(request):
    return HttpResponse("I am Raviteja")