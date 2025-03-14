from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Truck
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def signup(request):
    error_message = ''
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('trucks-index')
        else: 
            error_message = "Invalid sign up - try again"
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form, 'error_message': error_message})


class TruckCreate(LoginRequiredMixin, CreateView):
    model = Truck
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class TruckUpdate(LoginRequiredMixin, UpdateView):
    model = Truck
    fields = ['type','description','color']


class TruckDelete(LoginRequiredMixin, DeleteView):
    model = Truck
    success_url = '/trucks/'

@login_required
def truck_index(request):
    trucks = Truck.objects.filter(user=request.user)
    return render(request, 'trucks/index.html', {'trucks': trucks})

@login_required
def truck_detail(request, truck_id):
    truck = Truck.objects.get(id=truck_id)
    return render(request, 'trucks/detail.html', {'truck': truck})


def about(request):
    return render(request, 'about.html')

class Home(LoginView):
    template_name = 'home.html'


# class Truck:
#     def __init__(self, name, type, description, color):
#         self.name = name
#         self.type = type
#         self.description = description
#         self.color = color


# trucks = [
#         Truck('Big Foot', 'Classic', 'Kinda Old', 'Black '),
#         Truck('Mega Rex', 'Dino', 'New', 'Orange')
#     ]