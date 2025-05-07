"""
URL configuration for Rental_Management_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from . import settings
from django.conf.urls.static import static
from django.urls import path
from lavishBnB import views as f_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', f_views.Home, name ='Home'),
    path('properties/', f_views.properties, name ='properties'),
    path('cover/', f_views.cover, name ='cover'),
    path('rent_details/', f_views.rent_details, name ='rent_details'),
    path('upload_property/',f_views.upload_property,name='upload_property'),
    path('delete_property/<str:id>',f_views.delete_property,name = 'delete_property'),
    path('login/', f_views.user_login, name='login'),
    path('profile/', f_views.profile_view, name='profile'),
    path('signup/', f_views.signup_view, name='signup'),
    path('property/<int:id>/', f_views.property_details, name='property_details'),

              ]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
