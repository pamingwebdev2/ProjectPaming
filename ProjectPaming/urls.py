from django.conf.urls import url
from IReadApp import views

urlpatterns = [
    url(r'^$', views.LogPage, name='logpage'),
    url(r'^IReadApp/viewlist_url/$', views.ViewList, name='viewlist'),
    url(r'^IReadApp/newlist_url$', views.NewList, name='newlist'),
  
]

