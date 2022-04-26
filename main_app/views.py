from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse

from .models import Thing


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
  print(thing_id)
  amazingthing = Thing.objects.get(id=thing_id)
  return render(request, 'amazingthings/detail.html', { 'amazingthing': amazingthing })