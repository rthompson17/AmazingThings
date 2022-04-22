from django.shortcuts import render

class AmazingThing:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

amazingthings = [
  AmazingThing('Lolo', 'tabby', 'foul little demon', 3),
  AmazingThing('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  AmazingThing('Raven', 'black tripod', '3 legged cat', 4)
]


# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('this is the home view!')

def about(request):
    return render(request, 'about.html')

def amazingthings_index(request):
    return render(request, 'amazingthings/index.html', { 'amazingthings': amazingthings })