from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404
from lavishBnB import views as f_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Property, Category



# Create your views here.

def Home(request):
    featured_properties = Property.objects.all()
    context = {
        'featured_properties': featured_properties
    }
    return render(request, template_name='lavishBnB/home.html', context=context)


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
    city = request.GET.get('city')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    category = request.GET.get('category')
    if city:
        all_properties = all_properties.filter(location__city__icontains=city)
    if min_price:
        all_properties = all_properties.filter(price_per_night__gte=min_price)
    if max_price:
        all_properties = all_properties.filter(price_per_night__lte=max_price)
    if category:
        all_properties = all_properties.filter(category__id=category)

    context = {
        'all_properties': all_properties,
        'categories': Category.objects.all()  # For dropdown
    }
    return render(request, template_name='lavishBnB/Properties.html', context=context)


def properties_by_category(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    properties = Property.objects.filter(category=category)
    return render(request, 'properties_by_category.html', {
        'category': category,
        'properties': properties
    })


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

def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after saving
    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {'form': form})

    

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        messages.success(request, "Account created successfully!")
        return redirect('login')  # Better than redirecting to signup again

    return render(request, 'signup.html')




from django.shortcuts import render
from django.db.models import Q
from .models import Property

def search_results(request):
    query = request.GET.get('q', '').strip()  # Strips any leading/trailing whitespace from the query
    if query:
        # Filter properties based on the search query
        results = Property.objects.filter(
            Q(title__icontains=query) |
            Q(location__city__icontains=query) |
            Q(location__country__icontains=query)
        )
    else:
        # If no query is provided, return no results
        results = Property.objects.none()

    # If no results were found, set the message
    message = None
    if not results:
        message = f'No results found for "{query}". Try something else.'

    # Render the template with search query, results, and message
    return render(request, 'lavishBnB/search_results.html', {
        'query': query,
        'results': results,
        'message': message
    })



from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to login page after logout


def contact_us_view(request):
    return render(request, 'contact_us.html')

def send_message(request):
    return render(request, 'send_message.html')

def online_booking(request):
    return render(request, 'online_booking.html')

def helpline(request):
    return render(request, 'helpline.html')

def host_help(request):
    return render(request, 'host_help.html')

def guest_help(request):
    return render(request, 'guest_help.html')

def guidance(request):
    return render(request, 'guidance.html')


