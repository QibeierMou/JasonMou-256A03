from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from events.models import Event, Registration
from accounts.models import User
from django.utils import timezone

def is_admin(user):
    return user.role == 'admin'

def is_member(user):
    return user.role == 'member'

@login_required
def my_events(request):
    registrations = Registration.objects.filter(
        user=request.user
    ).order_by('event__start_date')

    return render(request, 'reports/my_events.html', {
        'registrations': registrations
    })

@login_required
def upcoming_events(request):
    events = Event.objects.filter(
        end_date__gte=timezone.now()
    ).order_by('start_date')

    return render(request, 'reports/upcoming.html', {
        'events': events
    })

@login_required
def all_events(request):
    if not is_admin(request.user):
        return render(request, 'reports/upcoming.html', {'events': []})

    events = Event.objects.all().order_by('start_date')

    return render(request, 'reports/all_events.html', {
        'events': events
    })

@login_required
def user_list(request):
    if not is_admin(request.user):
        return render(request, 'reports/user_list.html', {'users': []})

    users = User.objects.all().order_by('last_name')

    return render(request, 'reports/user_list.html', {
        'users': users
    })

@login_required
def event_people(request):
    if not is_admin(request.user) and not is_member(request.user):
        return render(request, 'reports/event_people.html', {'events': []})

    filter_type = request.GET.get('filter', 'upcoming')

    if filter_type == 'current':
        events = Event.objects.filter(
            start_date__lte=timezone.now(),
            end_date__gte=timezone.now()
        ).order_by('start_date')
    else:
        # all upcoming events
        events = Event.objects.filter(
            end_date__gte=timezone.now()
        ).order_by('start_date')

    return render(request, 'reports/event_people.html', {
        'events': events,
        'filter_type': filter_type
    })