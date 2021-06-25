from django.conf.urls import url
from IReadApp import views
from django.contrib import admin
from django.urls import include
from IReadApp import views as iread_views  
from IReadApp import urls as iread_urls




urlpatterns = [
    url('admin/',admin.site.urls),
    #url(r'^IReadApp/', include('iread_urls')),
    url('', include('IReadApp.urls')),
    # url(r'^donatepage/', iread_views.DonatePage, name='donatepage'),
    # url(r'^booklistpage/$', iread_views.BookList, name='booklistpage'),
    # url(r'^bookingpage/$', iread_views.BookingPage, name='bookingpage'),
    # url(r'^borrpage/$', iread_views.BorrPage, name='borrpage'),

    # url(r'^IReadApp/(\d+)/donatepage/$', views.DonatePage, name='donatepage'), #OK
    # url(r'^IReadApp/(\d+)/adddonate$', views.AddDonate, name='adddonate'),#OK

    # url(r'^IReadApp/booklistpage/$', views.BookList, name='booklistpage'), #OK
    # url(r'^IReadApp/addbooklist$', views.AddBookList, name='addbooklist'), #OK
    # # url(r'^IReadApp/updatebook/$', views.UpdateBook, name='updatebook'), 

    # url(r'^IReadApp/(\d+)/bookingpage/$', views.BookingPage, name='bookingpage'),#OK
    # url(r'^IReadApp/(\d+)/addbooking$', views.AddBooking, name='addbooking'), #OK

    # url(r'^IReadApp/borrpage', views.BorrPage, name='borrpage'),


    
    #---------------
    # 
    # 
    # 
    #------------

    # url(r'^IReadApp/viewlist_url/$', views.ViewList, name='viewlist'),
    # url(r'^IReadApp/(\d+)/$', views.ViewList, name='viewlist'),
    # url(r'^IReadApp/newlist_url$', views.NewList, name='newlist'),
    # url(r'^IReadApp/(\d+)/addItem$', views.AddItemLog, name='additem'),
]

#PROJECT URLS