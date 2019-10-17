from django.conf.urls import url
from . import views	
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_new_book$', views.add_new_book),
    url(r'^create_book$', views.create_book),    
    url(r'^view_book/(?P<book_id>\d+)$', views.view_book),
    url(r'^add_new_author$', views.add_new_author),
    url(r'^create_author$', views.create_author),    
    url(r'^view_author/(?P<author_id>\d+)$', views.view_author),
    url(r'^authors/(?P<author_id>\d+)/add_book$', views.add_book),
]