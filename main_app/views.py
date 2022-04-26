from asyncio import events
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse

from .models import Thing
from .forms import EventsForm

# Create your views here.
class ThingCreate(CreateView):
  model = Thing
  fields = '__all__'

class ThingUpdate(UpdateView):
  model = Thing
  fields = ['name', 'location', 'description', 'age']

class ThingDelete(DeleteView):
  model = Thing
  success_url = '/amazingthings/'  

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def amazingthings_index(request):
    amazingthings = Thing.objects.all()
    return render(request, 'amazingthings/index.html', { 'amazingthings': amazingthings })

def amazingthings_detail(request, thing_id):
  amazingthing = Thing.objects.get(id=thing_id)
  events_form = EventsForm() #generating the Events form

  return render(request, 'amazingthings/detail.html', { 'amazingthing': amazingthing, 'events_form': events_form })

def add_events(request, thing_id):
    form = EventsForm(request.POST)

    if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
      new_events = form.save(commit=False)
      #look at the note for the thing field in the Event model
      new_events.thing_id = thing_id
      new_events.save()
    return redirect('detail', thing_id=thing_id)
