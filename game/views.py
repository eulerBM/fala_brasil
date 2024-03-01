from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from game.models import tasks
from django.shortcuts import render

@login_required
def playing(request):
    
    task_user = tasks.objects.all()[:10]

    context = {
        'task': serialize('json', task_user),    
    }
    return render (request, 'game/playing.html', context)
