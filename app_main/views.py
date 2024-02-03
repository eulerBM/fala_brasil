from django.contrib.auth.decorators import login_required
from app_main.models import CustomUser
from django.shortcuts import render

@login_required
def home_page(request):
    return render(request, 'home/home.html')


@login_required
def friend_page(request):
    
    search_query = request.GET.get('search_query')

    useres_get = CustomUser.objects.filter(first_name__icontains=search_query)

    context = {
        'users': useres_get,
            
    }

    return render (request, 'friend/friend.html', context)
    
    

    
