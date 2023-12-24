from django.urls import path
from authen.views import login, logout

urlpatterns = [
    path('login/', login),
    path('logout/', logout),
]
