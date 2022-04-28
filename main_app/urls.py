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
    path('programs/', views.ProgramList.as_view(), name='programs_index'),
    path('programs/<int:pk>/', views.ProgramDetail.as_view(), name='programs_detail'),
    path('programs/create/', views.ProgramCreate.as_view(), name='programs_create'),
    path('programs<int:pk>/update/', views.ProgramUpdate.as_view(), name='programs_update'),
    path('programs/<int:pk>/delete', views.ProgramDelete.as_view(), name='programs_delete')
]