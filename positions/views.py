from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Position
from .forms import PositionForm

def is_admin(user):
    return user.role == 'admin'

@login_required
def position_list(request):
    if not is_admin(request.user):
        return redirect('event_list')

    positions = Position.objects.all().order_by('name')

    return render(request, 'positions/list.html', {
        'positions': positions
    })

@login_required
def position_create(request):
    if not is_admin(request.user):
        return redirect('event_list')

    form = PositionForm()

    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('position_list')

    return render(request, 'positions/form.html', {
        'form': form,
        'title': 'Create Position'
    })

@login_required
def position_update(request, id):
    if not is_admin(request.user):
        return redirect('event_list')

    position = get_object_or_404(Position, id=id)
    form = PositionForm(instance=position)

    if request.method == 'POST':
        form = PositionForm(request.POST, instance=position)
        if form.is_valid():
            form.save()
            return redirect('position_list')

    return render(request, 'positions/form.html', {
        'form': form,
        'title': 'Update Position'
    })

@login_required
def position_delete(request, id):
    if not is_admin(request.user):
        return redirect('event_list')

    position = get_object_or_404(Position, id=id)

    if request.method == 'POST':
        position.delete()
        return redirect('position_list')

    return render(request, 'positions/delete.html', {
        'position': position
    })