from django.db import models
from django.utils import timezone
import datetime
class Vehicle(models.Model):

    def __str__(self):
        return f"{self.vehicle_type} released on: {self.release_date.date()}"

    def was_released_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.release_date <= now

    vehicle_type = models.CharField(max_length=200)
    release_date = models.DateTimeField('date of release')

    was_released_recently.admin_order_field = 'release_date'
    was_released_recently.boolean = True
    was_released_recently.short_description = 'Released recently?'


class Brand(models.Model):

    def __str__(self):
        return f"{self.vehicle} -> {self.brand_name} costs {self.price}"

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=200)
    price = models.FloatField(default=0)
