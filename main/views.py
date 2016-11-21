""" Views for the main app """

from django.shortcuts import render
from main.forms import *
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
#from django.template import RequestContext


# Create your views here.

def index(request):
    """ Homepage """
    return render(request, 'index.html')

def login(request):
    """ User login page """
    return render(request, 'login.html')

@csrf_protect
def signup(request):
    """ User signup page """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            """ username is linked to email, also needed a username argument for create_user() """
            user = User.objects.create_user(username=form.cleaned_data['email'], first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'], email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()
    #variables = RequestContext(request, {'form': form})
    #return render('signup.html', variables)
    return render(request, 'signup.html')

def about(request):
    """ Cyqlo About Us page """
    return render(request, 'about.html')
