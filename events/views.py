from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Event, Registration
from .forms import EventForm
from positions.models import Position

def is_admin(user):
    return user.role == 'admin'

def is_member(user):
    return user.role == 'member'

def is_volunteer(user):
    return user.role == 'volunteer'

@login_required
def event_list(request):
    if is_admin(request.user):
        events = Event.objects.all().order_by('start_date')
    else:
        events = Event.objects.filter(
            end_date__gte=timezone.now()
        ).order_by('start_date')
    user_registrations = Registration.objects.filter(user=request.user)
    joined_event_ids = [r.event.id for r in user_registrations]
    return render(request, 'events/list.html', {
        'events': events,
        'joined_event_ids': joined_event_ids
    })

@login_required
def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    positions = Position.objects.all()
    if request.method == 'POST':
        position_id = request.POST.get('position')
        position = Position.objects.get(id=position_id)
        already_joined = Registration.objects.filter(
            user=request.user,
            event=event
        ).exists()
        if not already_joined:
            Registration.objects.create(
                user=request.user,
                event=event,
                position=position
            )
        return redirect('event_list')

    return render(request, 'events/detail.html', {
        'event': event,
        'positions': positions
    })

@login_required
def unregister(request, id):
    event = get_object_or_404(Event, id=id)
    Registration.objects.filter(
        user=request.user,
        event=event
    ).delete()
    return redirect('event_list')

@login_required
def create_event(request):
    if not is_admin(request.user):
        return redirect('event_list')
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
        positions = Position.objects.all()
    return render(request, 'events/form.html', {
        'form': form,
        'positions': positions
    })

@login_required
def update_event(request, id):
    event = get_object_or_404(Event, id=id)
    if not is_admin(request.user) and not is_member(request.user):
        return redirect('event_list')
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
        positions = Position.objects.all()
    return render(request, 'events/form.html', {
        'form': form, 
        'positions': positions
        })

@login_required
def delete_event(request, id):
    event = get_object_or_404(Event, id=id)
    if not is_admin(request.user):
        return redirect('event_list')
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'events/delete.html', {'event': event})