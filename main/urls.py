""" URLs for main app """

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login', views.login, name='login'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^about', views.about, name='about'),
    url(r'^routes', views.routes, name='routes'),
    url(r'^west_side_route', views.west_side_route, name='west_side_route'),
    url(r'^greenBronx_route', views.greenBronx_route, name='greenBronx_route'),
    url(r'^shore_parkway_route', views.shore_parkway_route, name='shore_parkway_route'),
    url(r'^pizza_tour_route', views.pizza_tour_route, name='pizza_tour_route'),
    url(r'^columbuscircle_bearmtn_route', views.columbuscircle_bearmtn_route, name='columbuscircle_bearmtn_route')
    
]
