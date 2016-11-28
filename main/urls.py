""" URLs for main app """

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login', views.login, name='login'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^about', views.about, name='about'),
    url(r'^routes', views.routes, name='routes'),
    url(r'^west_side_route', views.west_side_route, name='west_side_route')
]
