from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('amazingthings/', views.amazingthings_index, name='index'),
    path('amazingthings/<int:thing_id>/', views.amazingthings_detail, name='detail'),
    path('amazingthings/create/', views.ThingCreate.as_view(), name='things_create'),
    path('amazingthings/<int:pk>/update/', views.ThingUpdate.as_view(), name='things_update'),
    path('amazingthings/<int:pk>/delete/', views.ThingDelete.as_view(), name='things_delete'),
    path('amazingthings/<int:thing_id>/add_events/', views.add_events, name='add_events'),

]