from django.urls import path
from game.views import playing

urlpatterns = [
    path('playing', playing, name="playing"),
]
