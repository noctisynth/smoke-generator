from django.urls import path
from . import views

urlpatterns = [
    path("add", views.add),
    path("login", views.login),
    path("logout", views.logout),
    path("profile", views.profile),
    path("update", views.update),
]
