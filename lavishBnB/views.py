from django.contrib.auth.models import User
from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404
from lavishBnB import views as f_views


# Create your views here.

def Home(request):
    featured_properties = Property.objects.all()[:6]
    context = {
        'featured_properties': featured_properties
    }
    return render(request, template_name='lavishBnB/Home.html', context=context)


def cover(request):
    return render(request, template_name='cover.html')


def property_details(request, id):
    property = Property.objects.get(pk=id)
    context = {
        'property': property,
    }

    return render(request, template_name='lavishBnB/property_details.html', context=context)


def properties(request):
    all_properties = Property.objects.all()
    context = {
        'all_properties': all_properties
    }
    return render(request, template_name='lavishBnB/Properties.html', context=context)


def rent_details(request):
    return render(request, template_name='lavishBnB/rent_details.html')


def upload_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PropertyForm()

    return render(request, 'upload_property.html', {'form': form})


def update_property(request, id):
    property_obj = Property.objects.get(id=id)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property_obj)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PropertyForm(instance=property_obj)
    return render(request, 'update_property.html', {'form': form})


def delete_property(request, id):
    prop = get_object_or_404(Property, pk=id)
    if request.method == 'POST':
        prop.delete()
        return redirect('home')
    return render(request, 'delete_property.html', {'property': prop})


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # or any page after login
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'login.html')


def profile_view(request):
    user = request.user  # Make sure user is authenticated
    return render(request, 'profile.html', {'user': user})

def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('signup')

        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name
        user.save()

        messages.success(request, "Account created successfully!")
        return redirect('signup')  # or redirect to login page

    return render(request, 'signup.html')