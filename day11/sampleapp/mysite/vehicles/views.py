from .models import Vehicle
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'vehicles/index.html'
    context_object_name = 'vehicle_list'

    def get_queryset(self):
        return Vehicle.objects.all()



def vehicle_by_id(request,vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    brands = vehicle.brand_set.all()
    context = {"brands": brands}
    return render(request,'vehicles/vehicles.html',context)

def brand_by_id(request, vehicle_id, brand_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    brand = vehicle.brand_set.filter(pk=brand_id)
    context = {"brand" : brand[0]}
    return render(request, 'vehicles/brands.html',context)

def add(request):
    vehicles = Vehicle.objects.all()
    context = {"vehicle_list" : vehicles}
    return render(request, 'vehicles/add.html',context)

def insert(request):
    vehicle_id = request.POST['vehicle']
    vehicle = Vehicle.objects.get(pk=vehicle_id)
    brand_name = request.POST['item_name']
    price = request.POST['item_price']
    brand = vehicle.brand_set.create(brand_name = brand_name, price = price)
    brand.save()
    return HttpResponseRedirect(reverse('details', args=(vehicle_id,)))
