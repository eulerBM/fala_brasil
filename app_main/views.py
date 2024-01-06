from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home_page(request):
    return render(request, 'home/home.html')

def friend_page(request):
    return render (request, 'friend/friend.html')
    
    

    
