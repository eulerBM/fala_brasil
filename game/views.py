from django.contrib.auth.decorators import login_required
from game.models import tasks
from django.shortcuts import render

@login_required
def playing(request):
    task = tasks.objects.all()

    context = {
        'tasks': task,
            
    }
    return render (request, 'game/playing.html', context)
