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

    url(r'^IReadApp/(\d+)/donatepage/$', views.DonatePage, name='donatepage'), #OK
    url(r'^IReadApp/(\d+)/adddonate$', views.AddDonate, name='adddonate'),#OK
    url(r'^IReadApp/(\d+)/donatepage/updatedon/(?P<id>\d+)$', views.UpdateDon, name='updatedon'), 
    url(r'^IReadApp/(\d+)/donatepage/updatedon/statuschange/(?P<id>\d+)$', views.StatusChange, name='statuschange'), 
    url(r'^IReadApp/(\d+)/donatepage/deletedon/(?P<id>\d+)$', views.DeleteDon, name='deletedon'), 


    url(r'^IReadApp/booklistpage/$', views.BookList, name='booklistpage'), #OK
    url(r'^IReadApp/addbooklist$', views.AddBookList, name='addbooklist'), #OK
    url(r'^IReadApp/booklistpage/updatebook/(?P<id>\d+)$', views.UpdateBook, name='updatebook'), 
    url(r'^IReadApp/booklistpage/updatebook/bookchange/(?P<id>\d+)$', views.BookChange, name='bookchange'), 
    url(r'^IReadApp/booklistpage/deletebook/(?P<id>\d+)$', views.DeleteBook, name='deletebook'), 

    url(r'^IReadApp/(\d+)/bookingpage/$', views.BookingPage, name='bookingpage'),#OK
    url(r'^IReadApp/(\d+)/addbooking$', views.AddBooking, name='addbooking'), #OK

    url(r'^IReadApp/borrpage', views.BorrPage, name='borrpage'),


    #---------------
    # url(r'^IReadApp/donation/$', views.DonatePage, name='donatepage'),
    # url(r'^IReadApp/booklist/$', views.BookListPage, name='booklistpage'),
    # url(r'^IReadApp/status/$', views.BookingPage, name='bookingpage'),
    #------------

]

#APP URLS