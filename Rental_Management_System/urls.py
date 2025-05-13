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
    path('', f_views.Home, name='home'),
    path('properties/', f_views.properties, name ='properties'),
    path('cover/', f_views.cover, name ='cover'),
    path('rent_details/', f_views.rent_details, name ='rent_details'),
    path('upload_property/',f_views.upload_property,name='upload_property'),
    path('delete_property/<str:id>',f_views.delete_property,name = 'delete_property'),
    path('login/', f_views.user_login, name='login'),
    path('profile/', f_views.profile_view, name='profile'),
    path('signup/', f_views.signup_view, name='signup'),
    path('property/<int:id>/', f_views.property_details, name='property_details'),
    path('search/', f_views.search_results, name='search_results'),
    path('logout/', f_views.logout_view, name='logout'),
    path('contact-us/', f_views.contact_us_view, name='contact_us'),
    path('category/<str:category_name>/', f_views.properties_by_category, name='properties_by_category'),
    path('send-message/', f_views.send_message, name='send_message'),
    path('online-booking/', f_views.online_booking, name='online_booking'),
    path('helpline/', f_views.helpline, name='helpline'),
    path('host_help/', f_views.host_help, name='host_help'),
    path('guest_help/', f_views.guest_help, name='guest_help'),
    path('guidance/', f_views.guidance, name='guidance'),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
