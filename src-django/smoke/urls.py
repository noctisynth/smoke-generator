from django.urls import path
from smoke import views


urlpatterns = [
    path("generate", views.generate),
    path("joint", views.joint),
    path("generate_history", views.generate_history),
    path("joint_history", views.joint_history),
    path("styles", views.styles),
    path("masks", views.masks),
    path("delete", views.delete),
    path("update", views.update),
    path("get", views.get),
    path("get_public", views.get_public),
    path("explore_add", views.explore_add),
]
