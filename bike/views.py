from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Bike

# Create your views here.


class BikeListView(ListView):
    template_name = 'bikes/bike_list.html'
    model = Bike


class BikeDetailView(DetailView):
    template_name = 'bikes/bike_detail.html'
    model = Bike


class BikeCreateView(CreateView):
    template_name = 'bikes/bike_create.html'
    model = Bike
    fields = ['name', 'purchaser', 'desc']


class BikeUpdateView(UpdateView):
    template_name = 'bikes/bike_update.html'
    model = Bike
    fields = ['name', 'purchaser', 'desc']


class BikeDeleteView(DeleteView):
    template_name = 'bikes/bike_delete.html'
    model = Bike
    success_url = reverse_lazy('bike_list')