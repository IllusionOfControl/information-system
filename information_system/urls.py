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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from information_system import settings
from information_system.apps.core import views as core_views

urlpatterns = [
    path("admin/", admin.site.urls),

    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', next_page='profile'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/logout.html'), name='logout'),

    path('profile/', core_views.profile, name='profile'),
    path('', core_views.index, name='index'),
    path('departments/', core_views.department_list, name='department_list'),
    path('devices/', core_views.device_list, name='device_list'),
    path('device_models/', core_views.device_model_list, name='device_model_list'),
    path('repairs/', core_views.repair_list, name='repair_list'),
    path('export_repairs_to_excel/', core_views.export_repairs_to_excel, name='export_repairs_to_excel'),
    path('maintenance/', core_views.maintenance_list, name='maintenance_list'),
    path('export_maintenance_to_excel/', core_views.export_maintenance_to_excel, name='export_maintenance_to_excel'),

    path('repairs/create/', core_views.create_repair, name='create_repair'),
    path('repairs/<int:repair_id>/edit/', core_views.edit_repair, name='edit_repair'),
    path('repairs/<int:repair_id>/delete/', core_views.delete_repair, name='delete_repair'),

    path('maintenance/create/', core_views.create_maintenance, name='maintenance-create'),
    path('maintenance/<int:maintenance_id>/edit/', core_views.edit_maintenance, name='maintenance-edit'),
    path('maintenance/<int:maintenance_id>/delete/', core_views.delete_maintenance, name='maintenance-delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
