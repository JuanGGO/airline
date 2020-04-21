from django.shortcuts import render, Http404
from .models import Flight, Passenger


# Create your views here.
def index(request):
    context = {
        'flights': Flight.objects.all()
    }
    return render(request, 'flights/index.html', context)


def flight(request, flight_id):
    try:
        f = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        return Http404("Flight does not exists")
    context = {
        'flight': f,
        'passengers': f.passengers.all()
    }

    return render(request, 'flights/flight.html', context)
