from django.conf.urls import url
from IReadApp import views

urlpatterns = [
    url(r'^$', views.LogPage, name='logpage'),
  
]

