from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:vehicle_id>/',views.vehicle_by_id, name='details'),
    path('<int:vehicle_id>/brands/<int:brand_id>/',views.brand_by_id, name='brand'),
    path('add/',views.AddView.as_view(),name='add'),
    path('insert/',views.insert, name='insert')
]