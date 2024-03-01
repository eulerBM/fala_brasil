from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app_main.models import CustomUser

@login_required
def friend_page(request):

    search_query = request.GET.get('search_query')

    useres_get = CustomUser.objects.filter(first_name__icontains=search_query)

    context = {
        'users': useres_get,   
    }
    return render (request, 'friend/friend.html', context)

@login_required
def add_friend(request):
    pass

@login_required
def visualizer_friend(request):
    pass
