from django.shortcuts import render, redirect
# from asyncio import events
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from django.http import HttpResponse
from .models import Thing, Program
from .forms import EventsForm

# Create your views here.
class ThingCreate(CreateView):
  model = Thing
  fields = ['name', 'location', 'description', 'age']

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
  programs_thing_doesnt_have = Program.objects.exclude(id__in = amazingthing.programs.all().values_list('id')) #try thing.programs
  events_form = EventsForm()
  return render(request, 'amazingthings/detail.html', {
    'amazingthing': amazingthing, 'events_form': events_form,
    'programs': programs_thing_doesnt_have
  })


def add_events(request, thing_id):
    form = EventsForm(request.POST)

    if form.is_valid():
      new_events = form.save(commit=False)
      new_events.thing_id = thing_id
      new_events.save()
    return redirect('detail', thing_id=thing_id)



def assoc_program(request, thing_id, program_id):
  Thing.objects.get(id=thing_id).programs.add(program_id)
  return redirect('detail', thing_id=thing_id)



class ProgramList(ListView):
  model = Program

class ProgramDetail(DetailView):
  model = Program

class ProgramCreate(CreateView):
  model = Program
  fields = '__all__'

class ProgramUpdate(UpdateView):
  model = Program
  fields = ['name', 'kind']

class ProgramDelete(DeleteView):
  model = Program
  success_url = '/programs/'