from django.urls import path
from . import views

urlpatterns = [
    path("generate", views.generate),
    path("joint", views.joint),
    path("generate_history", views.generate_history),
    path("joint_history", views.joint_history),
    path("styles", views.styles),
    path("masks", views.masks),
    path("delete", views.delete),
    path("update", views.update),
]
