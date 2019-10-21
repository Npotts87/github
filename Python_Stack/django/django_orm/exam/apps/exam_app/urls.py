from django.conf.urls import url
from . import views	
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^logout$', views.logout),
    url(r'^create_user$', views.create_user),
    url(r'^process_login$', views.login),
    url(r'^add_new_user_successful$', views.add_new_user_successful),
    url(r'^user_home$', views.user_home),
    # Renders the form to enter a new trip
    url(r'^add_trip_form$', views.add_trip_form),
    # Form sends data to this url
    url(r'^add_trip_save$', views.add_trip_save),
]