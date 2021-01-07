from django.shortcuts import render
from .models import Event
from participants.models import Participant

# Create your views here.

def event_list(request):
    events = Event.objects.all()
    return render(request,'event_list.html',{'event':events})

def home(request):
    context = {}
    events = Event.objects.all()
    context['events'] = events
    return render(request,'home.html',context)


