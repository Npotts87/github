from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.index),
    url(r'^(?P<nums>\d+)$', views.nums),
    url(r'^(?P<nums>\d+)/edit$', views.nums_edit),
    url(r'^(?P<nums>\d+)/delete$', views.nums_delete),
]