"""
URL configuration for smokegenerator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings

admin.site.site_header = "烟雾生成拼接系统"
admin.site.site_title = "烟雾生成拼接系统"
admin.site.index_title = "烟雾生成拼接系统"


def for_admin(_):
    return HttpResponseRedirect("/admin/")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("admin", for_admin),
    path("", TemplateView.as_view(template_name="index.html")),
    path("account/", include("account.urls")),
    path("billboard/", include("billboard.urls")),
    path("smoke/", include("smoke.urls")),
    re_path("^(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
]
