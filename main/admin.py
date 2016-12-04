""" Custom admin code """

from django.contrib import admin
from .models import Route #User, Route

#Registers models to admin site
#admin.site.register(User)
admin.site.register(Route)
