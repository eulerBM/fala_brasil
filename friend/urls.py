from django.urls import path
from friend.views import friend_page

urlpatterns = [
    path('playing', friend_page, name="search_player"),
    
]
