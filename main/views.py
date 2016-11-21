""" Views for the main app """

from django.shortcuts import render
from main.forms import *
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    """ Homepage """
    return render(request, 'index.html')

def login(request):
    """ User login page """
    return render(request, 'login.html')

@csrf_protect
def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create(first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'], email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'signup.html')

def about(request):
    """ Cyqlo About Us page """
    return render(request, 'about.html')
