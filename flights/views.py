from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Flight, Passenger, User

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    non_passenger = Passenger.objects.exclude(flights=flight).all()
    
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": non_passenger.all(),
    })

def book(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    
    if request.method == "POST":
        passenger_id = request.POST.get("passenger")
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id,))) 
    
    return render(request, "flights/book.html", {
        "flights": Flight.objects.all(),
        "passengers": Passenger.objects.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
        
    })
