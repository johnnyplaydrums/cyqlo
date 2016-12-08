""" URLs for main app """

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^login_view', views.login_view, name='login_view'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^logout_view', views.logout_view, name='logout_view'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^route_search', views.route_search, name='route_search'),

    # Cyqlo cycling routes
    url(r'^routes_page', views.routes_page, name='routes_page'),
    url(r'^west_side_route', views.west_side_route, name='west_side_route'),
    url(r'^bronx_green_lands', views.bronx_green_lands, name='bronx_green_lands'),
    url(r'^shore_parkway_route', views.shore_parkway_route, name='shore_parkway_route'),
    url(r'^cunningham_park_trail', views.cunningham_park_trail, name='cunningham_park_trail'),
    url(r'^columbuscircle_bearmtn_route', views.columbuscircle_bearmtn_route, name='columbuscircle_bearmtn_route'),
    url(r'^prospect_coneyisland_route', views.prospect_coneyisland_route, name='prospect_coneyisland_route'),

    # Cyqlo themed routes
    url(r'^pizza_tour_route', views.pizza_tour_route, name='pizza_tour_route'),
    url(r'^harlem_soulfood_tour', views.soulfood_harlem, name='soulfoodHarlem'),
    url(r'^ramen_tour', views.ramen_tour, name='ramen_tour'),
    url(r'^hamilton_tour', views.hamilton_tour, name='hamilton_tour'),
]
