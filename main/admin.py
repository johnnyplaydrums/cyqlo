""" Custom admin code """

from django.contrib import admin
from .models import Route

#Registers models to admin site

admin.site.register(Route)
