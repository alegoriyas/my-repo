"""
Definition of urls for learning_logs.
"""

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    
    #Sign in
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),

    #Sign out
    url(r'^logout/$', views.logout_view, name='logout'),

    #Registration page
    url(r'^register/$', views.register, name='register'),

]