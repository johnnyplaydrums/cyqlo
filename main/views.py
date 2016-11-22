""" Views for the main app """

from django.shortcuts import render
from main.forms import RegistrationForm
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    """ Homepage """
    return render(request, 'index.html')

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
    return render(request, 'routes.html')
