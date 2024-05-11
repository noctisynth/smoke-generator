from django.urls import path
from . import views

urlpatterns = [
    path("latest", views.latest),
    path("all", views.all),
    path("get/<int:aid>", views.get),
]
