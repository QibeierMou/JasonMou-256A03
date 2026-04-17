from django.urls import path
from . import views

urlpatterns = [
    path('my-events/', views.my_events, name='my_events'),
    path('upcoming/', views.upcoming_events, name='upcoming_events'),
    path('all-events/', views.all_events, name='all_events'),
    path('users/', views.user_list, name='user_list'),
    path('event-people/', views.event_people, name='event_people'),
]