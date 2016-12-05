""" Views for the main app """

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, authenticate
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from main.forms import RegistrationForm, LoginForm
from main.models import Route

# Create your views here.

def index(request):
    """ Homepage """
    routes = Route.objects.all()
    return render(request, 'index.html', {'routes': routes})

# Django already have builtin login function, can't reuse login
def login_view(request):
    """ User login page """
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if User.objects.filter(username=username):
                if user is not None:
                    auth.login(request, user)
                    return HttpResponseRedirect('profile')
            else:
                return render(request, 'login.html', {'form':form})
    else:
        return render(request, 'login.html', {'form':form})
    return render(request, 'login.html', {'form':form})

def signup(request):
    """ User signup page """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            if User.objects.filter(username=username):
                form = RegistrationForm()
                return render(request, 'signup.html', {'form':form})
            else:
                user = User.objects.create_user(username, email, password)
                user.save()
                user = authenticate(username=username, password=password)
                auth.login(request, user)
                return HttpResponseRedirect('profile')
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form':form})

# Django already have builtin logout function, can't reuse logout
def logout_view(request):
    """ User logout page """
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/login_view')
def profile(request):
    """ User profile page """
    return render(request, 'profile.html')

def about(request):
    """ Cyqlo About Us page """
    return render(request, 'about.html')

def routes_page(request):
    """ Routes listing page """
    routes = Route.objects.all()
    return render(request, 'routes-page.html', {'routes': routes})

def west_side_route(request):
    """ Serve the West Side Route"""
    return render(request, 'west_side_route.html')

def shore_parkway_route(request):
    """ Serve the Shore Parkway Route """
    return render(request, 'shore_parkway_route.html')

def green_bronx_route(request):
    """ Serve the greenBronx Route """
    return render(request, 'green_bronx_route.html')

def pizza_tour_route(request):
    """ Serve the Pizza Tour Route """
    return render(request, 'pizza_tour_route.html')

def columbuscircle_bearmtn_route(request):
    """ Serve the Manhattan to Bear Mountain Route """
    return render(request, 'columbuscircle_bearmtn_route.html')

def cunningham_park_trail(request):
    """ Serve the Cunningham Park Mountain Bike Trail """
    return render(request, 'cunningham_park_trail.html')
