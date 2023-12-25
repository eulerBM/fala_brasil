from django.urls import path
from authen.views import login_auth, logout_auth

urlpatterns = [
    path('login/', login_auth, name="login_auth"),
    path('logout/', logout_auth, name="logout_auth"),
]
