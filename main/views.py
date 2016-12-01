""" Views for the main app """

from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import RegistrationForm
from main.models import Route

# Create your views here.

def index(request):
    """ Homepage """
    routes = Route.objects.all()
    return render(request, 'index.html', {'routes': routes})

def login(request):
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

def about(request):
    """ Cyqlo About Us page """
    return render(request, 'about.html')

def routes(request):
    """ Routes listing page """
    return render(request, 'routes-page.html')

def west_side_route(request):
    """ Serve the West Side Route"""
    return render(request,  'west_side_route.html')

def shore_parkway_route(request):
    """ Serve the Shore Parkway Route """
    return render(request, 'shore_parkway_route.html')

def greenBronx_route(request):
    """ Serve the greenBronx Route """
    return render(request, 'greenBronx_route.html')
def columbuscircle_bearmtn_route(request):
    """ Serve the Manhattan to Bear Mountain Route """
    return render(request, 'columbuscircle_bearmtn_route.html')
