from django.shortcuts import render,redirect


from .forms import RegisterForm
from .models import Participant
#from events.models import Event
#from events.views import home

# Create your views here.

def registration(request):
    context = {}
    # if request.POST:
    #     form = RegisterForm(request.POST)
    #     context['form'] = form
    #     if form.is_valid():
    #         form.save()
    #         #context = {}
    #         #events = Event.objects.all()
    #         #context['events'] = events
    #         return redirect("home")
        
    #     else :
    #         context['form'] = form
    #         form = RegisterForm()
    if request.method == 'GET': 
        return render(request, 'form.html', {'form': RegisterForm()}) 
    else: 
        form = RegisterForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            print("Success form filled")
            return redirect("home")
            #return redirect("home")
    

    #context['form'] = form
    
    #return render(request,'form.html',context)
