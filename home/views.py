from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Pricing,Trainers
from .forms import BookingForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def features(request):
    return render(request, 'features.html')

def pricing(request):
    dict_price={
        'pri' : Pricing.objects.all()
    }
    return render(request, 'pricing.html',dict_price)

def trainers(request):
    dict_tri={
        'tri':Trainers.objects.all()
    }
    return render(request, 'trainers.html',dict_tri)

def blog(request):
    if request.method =="POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirm.html')
    form = BookingForm()
    dict_form={
        'form':form
    }
    return render(request, 'blog.html',dict_form)
