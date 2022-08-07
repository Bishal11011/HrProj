from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', home, name="home"),
    path('loginregister/', loginregister, name="loginregister"),
    path('profile/<str:id>/', profile, name="profile"),
    path("logout/", log_out, name="logout"),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', VerificationView.as_view(), name="activate")
    
]

