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
    routes = Route.objects.filter(tags__contained_by=[''])
    themed = Route.objects.filter(tags__contains=['themed'])
    return render(request, 'index.html', {'routes': routes, 'themed': themed})

def about(request):
    """ Cyqlo About Us page """
    return render(request, 'about.html')

def routes_page(request):
    """ Routes listing page """
    routes = Route.objects.filter(tags__contained_by=[''])
    themed = Route.objects.filter(tags__contains=['themed'])
    return render(request, 'routes-page.html', {'routes': routes, 'themed': themed})

def route_search(request):
    """ Route search query """
    query = request.POST
    duration = int(query.__getitem__('time'))
    durationdiff = duration * .6
    distance = int(query.__getitem__('distance'))
    distancediff = distance * .6
    difficulty = query.__getitem__('difficulty')
    if difficulty == 'any':
        routes = Route.objects.filter(
            duration__range=(duration - durationdiff, duration + durationdiff),
            distance__range=(distance - distancediff, distance + distancediff),
            tags__contained_by=['']
        )
    else:
        routes = Route.objects.filter(
            duration__range=(duration - durationdiff, duration + durationdiff),
            distance__range=(distance - distancediff, distance + distancediff),
            difficulty=difficulty,
            tags__contained_by=['']
        )

    if len(routes) == 0:
        no_results = True
        routes = Route.objects.filter(tags__contained_by=[''])
    else:
        no_results = False

    themed = Route.objects.filter(tags__contains=['themed'])
    return render(request, 'routes-page.html', {'routes': routes, 'no_results':no_results, 'themed': themed})

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

def team(request):
    """ Cqylo team page """
    return render(request, 'team.html')

# Cyqlo cycling routes
def west_side_route(request):
    """ Serve the West Side Route"""
    return render(request, 'west_side_route.html')

def shore_parkway_route(request):
    """ Serve the Shore Parkway Route """
    return render(request, 'shore_parkway_route.html')

def bronx_green_lands(request):
    """ Serve the route to Van Cortlandt House Museum to Orchard Beach """
    return render(request, 'bronx_green_lands.html')

def columbuscircle_bearmtn_route(request):
    """ Serve the Manhattan to Bear Mountain Route """
    return render(request, 'columbuscircle_bearmtn_route.html')

def cunningham_park_trail(request):
    """ Serve the Cunningham Park Mountain Bike Trail """
    return render(request, 'cunningham_park_trail.html')

def prospect_coneyisland_route(request):
    """ Serve the Prospect Park to Coney Island Beach Route """
    return render(request, 'prospect_coneyisland_route.html')

# Cyqlo themed routes
def pizza_tour_route(request):
    """ Serve the Pizza Tour Route """
    return render(request, 'pizza_tour_route.html')

def soulfood_harlem(request):
    """ Serve the Harlem Soul Food tour """
    return render(request, 'harlem_soulfood_tour.html')

def hamilton_tour(request):
    """ Serve the Hamilton historic tour """
    return render(request, 'hamilton_tour.html')

def ramen_tour(request):
    """ Serve the Ramen Tour """
    return render(request, 'ramen_tour.html')

def central_park_full_loop(request):
    """ Serve the Central Park Full Loop"""
    return render(request, 'central_park_full_loop.html')

def central_park_nohill_loop(request):
    """ Serve the Central Park Full Loop"""
    return render(request, 'central_park_nohill_loop.html')
