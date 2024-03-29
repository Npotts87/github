from django.conf.urls import url
from . import views	
                    
urlpatterns = [
    url(r'^$', views.front_door),
    # url(r'^$', views.index),
    url(r'^create_user$', views.create_user),
    url(r'^add_new_user_successful$', views.add_new_user_successful),
    url(r'^process_login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^dashboard$', views.dashboard),
    url(r'^user_settings$', views.user_settings),
    url(r'^wish_list$', views.wish_list),
    url(r'^shopping_cart$', views.shopping_cart),
    url(r'^order_complete$', views.order_complete),
    url(r'^previous_orders$', views.previous_orders),

    # url(r'^item/view/(?P<id>\d+)$', views.view_item),
# 
    # url(r'^remove_item/(?P<id>\d+)$', views.remove_item),

    #url(r'^add_job_form$', views.add_job_form),
    #url(r'^create_job$', views.create_job),
    #url(r'^add_job_save$', views.add_job_save),
    #url(r'^jobs/edit/(?P<id>\d+)$', views.edit_job),
    #url(r'^jobs/edit_form/(?P<id>\d+)$', views.edit_job_form),
]