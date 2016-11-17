from django.db import models
from django.contrib.postgres.fields import ArrayField

#Data representation of a user
class User(models.Model):
    first_name = models.CharField(max_length = 50, null=False, blank=False)
    last_name = models.CharField(max_length = 50, null=False, blank=False)
    email = models.EmailField(max_length = 50, null=False, blank=False, unique=True)
    password = models.CharField(max_length=256, null=False, blank=False)
    
#Data representation of a route
class Route(models.Model):
    route_name = models.CharField(max_length = 50, null=False, blank=False)
    duration = models.DurationField(null=False, blank=False) # uses postgres interval format 'day:hr:min', for ex, 1 day is 01:00:00
    origin = ArrayField(models.FloatField(null=False, blank=False), size=2) #[lat,lng]
    destination = ArrayField(models.FloatField(null=False, blank=False), size=2) #[lat,lng]
    waypoints = ArrayField(models.CharField(max_length=256,null=False, blank=False)) #[location1, location2, location3, ...]

