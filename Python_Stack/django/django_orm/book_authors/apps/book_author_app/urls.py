from django.conf.urls import url
from . import views	# the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_new_book$', views.add_new_book),
    url(r'^view_book$', views.view_book),
    url(r'^add_new_author$', views.add_new_author),
    url(r'^view_author$', views.view_author),
]