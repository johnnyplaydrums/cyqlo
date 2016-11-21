""" Views for the main app """

from django.shortcuts import render

# Create your views here.

def index(request):
    """ Homepage """
    return render(request, 'index.html')

def login(request):
    """ User login page """
    return render(request, 'login.html')

def signup(request):
    """ User signup page """
    return render(request, 'signup.html')

def about(request):
    """ Cyqlo About Us page """
    return render(request, 'about.html')

def routes(request):
    """ Routes listing page """
    return render(request, 'routes.html')
