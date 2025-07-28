from django.urls import path
from . import views


# urlpatterns below

urlpatterns = [
    #Auth routes
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    #Other routes
    path("", views.home, name="home"),
    #path("profile/", views.profile_view, name="profile"),
]
