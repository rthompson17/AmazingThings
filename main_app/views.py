from django.shortcuts import render

# class AmazingThing:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, location, description, age):
#     self.name = name
#     self.location = location
#     self.description = description
#     self.age = age

# amazingthings = [
#   AmazingThing('Underwater Forest', 'Kaindy Lake, Kazakhstan', 'The sunken forest is part of a 400 meter long Lake Kaindy in Kazakhstan’s portion of the Tian Shan Mountains located 129 km from the city of Almaty. The lake was created as the result of an enormous limestone landslide, triggered by the 1911 Kebin earthquake.', 111),
#   AmazingThing('The Ghost Trees', 'Pakistan', 'The eye-catching phenomenon is an unexpected side-effect of the flooding in parts of Pakistan. Millions of spiders climbed up into the trees to escape the rising flood waters, shrouding them with their silky webs. Because of the scale of the flooding and the fact that the water has taken so long to recede, many trees have become cocooned in ghostly spiders webs.', 12),
#   AmazingThing('Reflective Salt Flats', 'Bolivia', 'The Salar was formed as a result of transformations between several prehistoric lakes. It is covered by a few meters of salt crust, which has an extraordinary flatness with the average altitude variations within one meter over the entire area of the Salar. When it rains, this flat surface forms the largest mirror in the world.', 'Unknown')
# ]


# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def amazingthings_index(request):
    return render(request, 'amazingthings/index.html', { 'amazingthings': amazingthings })