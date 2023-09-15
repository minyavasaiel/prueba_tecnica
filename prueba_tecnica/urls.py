"""
URL configuration for prueba_tecnica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from prueba_tecnica import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('logout/', views.logout_view, name='logout'),
    path('readjason/', views.read_json, name='read_json'),
    path('organizations-list/', views.listar, name= 'organizations-list'),
    path('centers-list/', views.listarCentros, name= 'centers-list'),
    path('add-organization/', views.add_organization, name= 'add-organization'),
    path('add-center/', views.add_center, name= 'add-center'),
    path('added-organization/', views.added_organization, name= 'added-organization'),
    path('added-center/', views.added_center, name= 'added-center'),
    path('detail-organization/<int:id>/', views.detail_organization, name= 'detail-organization'),
    path('detail-center/<int:id>/', views.detail_center, name= 'detail-center'),
    path('updated-organization/<int:id>/', views.updated_organization, name= 'updated-organization'),
    path('updated-center/<int:id>/', views.updated, name= 'updated-center'),
    path('delete-organization/<int:id>/', views.delete_organization, name= 'delete-organization'),
    path('delete-center/<int:id>/', views.delete_center, name= 'delete-center'),

]
