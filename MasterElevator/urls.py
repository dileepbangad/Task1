from django.urls import path,include
from .views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('addelevator',AddNewElevatorAPIView.as_view()), #Initialise the elevator system to create ‘n’ elevators in the system
    path('requestelevator',RequestElevatorAPIView.as_view()), #create a request by the user for the elevator
    path('fetchelevatorrequests',FetchRequestAPIView.as_view()), #Fetch all requests for a given elevator and Saves user request to the list of requests for a elevator
    path('fetchnextdestrequests',FetchNextDestAPIView.as_view()), #Fetch the next destination floor for a given elevator and Fetch if the elevator is moving up or down currently
    path('markisoperatable',MarkOperationalStatusAPIView.as_view()), #Mark a elevator as not working or in maintenance and vice-versa to continue also
    path('openclose',OpenCloseAPIView.as_view()), #Open/close the door, and also show the current-floor and next upcoming floor
]