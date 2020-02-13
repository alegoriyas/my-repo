"""
Definition of urls for learning_logs.
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    # Page home (index)
    url(r'^$', views.index, name='index'),
    
    # Conclusion of all topics
    url(r'^topics/$', views.topics, name='topics'),

    # Page with detailed information on a specific topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # Page for adding a new topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    # Page for adding a new record
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    # Page for editing an entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]