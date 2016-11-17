from django.contrib import admin
from .models import User, Route

#Registers models to admin site
admin.site.register(User)
admin.site.register(Route)
