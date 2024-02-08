from django.urls import path
from friend.views import friend_page, add_friend, visualizer_friend


urlpatterns = [
    path('playing', friend_page, name="search_player"),
    path('add_friend', add_friend, name="add_player"),
    path('visualizer_friend', visualizer_friend, name="visualizer_player"),
    
]
