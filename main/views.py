""" Views for the main app """

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from main.forms import RegistrationForm
from main.models import Route

# Create your views here.

def index(request):
    """ Homepage """
    routes = Route.objects.all()
    return render(request, 'index.html', {'routes': routes})

# Django already have builtin login function, can't reuse login
def login_view(request):
    """ User login page """
    return render(request, 'login.html')

def signup(request):
    """ User Signup page """
    # Form is initially empty
    form = None
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'signup.html', {'form': form})

# Django already have builtin logout function, can't reuse logout
def logout_view(request):
    """ User logout page """
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/login_view')
def profile(request):
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
