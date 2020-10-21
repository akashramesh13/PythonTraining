from django.http import HttpResponse
from .models import Vehicle,Brand
from django.shortcuts import get_object_or_404
from django.template import loader
from django.shortcuts import render
import json
def index(request):

    vehicles = Vehicle.objects.all()

    context = {
        'vehicle_list': vehicles,
    }
    return render(request,'vehicles/index.html',context)


def vehicle_by_id(request,vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    brands = vehicle.brand_set.all()
    brands_dict = {brand.id : (brand.brand_name, brand.price)for brand in brands }
    return HttpResponse(json.dumps(brands_dict))

def brand_by_id(request, vehicle_id, brand_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    brand = vehicle.brand_set.filter(pk=brand_id)
    context = {"brand" : brand[0]}
    return render(request, 'vehicles/brands.html',context)