from django.conf.urls import url
from . import views	
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^create_user', views.create_user),
    url(r'^process_login', views.login),
    url(r'^add_new_user_successful/(?P<user_id>\d+)$', views.view_user),

]