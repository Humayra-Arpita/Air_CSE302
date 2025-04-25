from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
# Create your views here.

def Home(request):
    featured_properties = Property.objects.all()[:6]
    context = {
        'featured_properties': featured_properties
    }
    return render(request, template_name='lavishBnB/Home.html', context = context)

def properties(request):
    all_properties = Property.objects.all()
    context = {
        'all_properties': all_properties
    }
    return render(request, template_name='lavishBnB/Properties.html', context = context)

def rent_details(request):
    return render(request, template_name='lavishBnB/rent_details.html')

