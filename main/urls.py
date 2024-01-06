from django.contrib import admin
from django.urls import path, include
from app_main.views import home_page, friend_page

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('friend/', friend_page, name='friend'),

    #includes
    path('game/', include('game.urls')),
    path('auth/', include('authen.urls')),
]
