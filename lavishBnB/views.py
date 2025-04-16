from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def Home(request):
    return render(request, template_name='lavishBnB/Home.html')

def properties(request):
    return render(request, template_name='lavishBnB/Properties.html')

def rent_details(request):
    return render(request, template_name='lavishBnB/rent_details.html')
