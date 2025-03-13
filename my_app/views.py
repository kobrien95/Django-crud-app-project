from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
class Truck:
    def __init__(self, name, type, description, color):
        self.name = name
        self.type = type
        self.description = description
        self.color = color


trucks = [
        Truck('Big Foot', 'Classic', 'Kinda Old', 'Black '),
        Truck('Mega Rex', 'Dino', 'New', 'Orange')
    ]

def truck_index(request):
    return render(request, 'trucks/index.html', {'trucks': trucks})

def home(request):
    return HttpResponse('<h1>Hello Monster Truck Collector</h1>')

def about(request):
    return render(request, 'about.html')

