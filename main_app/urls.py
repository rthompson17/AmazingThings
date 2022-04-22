from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('amazingthings/', views.amazingthings_index, name='index'),
]