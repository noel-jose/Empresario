from django.shortcuts import render

from .forms import RegisterForm
from .models import Participant
from events.models import Event
from events.views import home

# Create your views here.

def registration(request):
    context = {}
    if request.POST:
        form = RegisterForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            context = {}
            events = Event.objects.all()
            context['events'] = events
            return render(request,'home.html',context)
        
        else :
            context['form'] = form
            form = RegisterForm()
            
    

    #context['form'] = form
    return render(request,'form.html',context)
