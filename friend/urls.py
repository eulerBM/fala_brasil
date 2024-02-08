from django.urls import path
from friend.views import friend_page, add_friend


urlpatterns = [
    path('playing', friend_page, name="search_player"),
    path('add_friend', add_friend, name="add_player"),
    
]
