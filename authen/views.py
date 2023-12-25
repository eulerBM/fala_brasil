from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def login_auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            return redirect('home')
    
    
    return render(request, 'auth/login.html')


def logout_auth(request):
    logout(request)
    return redirect('login_auth')