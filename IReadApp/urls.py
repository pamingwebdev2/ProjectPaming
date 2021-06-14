from django.conf.urls import url
from IReadApp import views
# from django.contrib import admin

urlpatterns = [
    # url(r'^$', views.WelcomePage, name='welcpage'),
    # url(r'^$', views.AdvocacyPage, name='advocacypage'),
    url(r'^$', views.LogPage, name='logpage'),
    # url('admin/',admin.site.urls),
    # url(r'^IReadApp/viewlist_url/$', views.ViewList, name='viewlist'),
    url(r'^IReadApp/(\d+)/$', views.ViewList, name='viewlist'),
    url(r'^IReadApp/newlist_url$', views.NewList, name='newlist'),
    url(r'^IReadApp/(\d+)/addItem$', views.AddItemLog, name='additem'),

    #---------------
    # url(r'^IReadApp/donation/$', views.DonatePage, name='donatepage'),
    # url(r'^IReadApp/booklist/$', views.BookListPage, name='booklistpage'),
    # url(r'^IReadApp/status/$', views.BookingPage, name='bookingpage'),
    #------------

]

#APP URLS