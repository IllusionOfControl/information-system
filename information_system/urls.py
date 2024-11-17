"""
URL configuration for information_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from information_system.apps.core import views as core_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', core_views.index, name='index'),
    path('departments/', core_views.department_list, name='department_list'),
    path('devices/', core_views.device_list, name='device_list'),
    path('device_models/', core_views.device_model_list, name='device_model_list'),
]
