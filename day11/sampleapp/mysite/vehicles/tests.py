from django.test import TestCase
import datetime
from django.utils import timezone
from django.test import Client
from .models import Vehicle
from django.urls import reverse

def create_vehicle(vehicle_type, days):

    time = timezone.now() + datetime.timedelta(days=days)
    return Vehicle.objects.create(vehicle_type = vehicle_type, release_date=time)

class VehicleModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Vehicle(release_date=time)
        self.assertIs(future_question.was_released_recently(), False)
    
    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Vehicle(release_date=time)
        self.assertIs(old_question.was_released_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Vehicle(release_date=time)
        self.assertIs(recent_question.was_released_recently(), True)

class VehicleIndexViewTest(TestCase):

    def test_client_response(self):
        self.client = Client()
        create_vehicle(vehicle_type="Past Vehicle", days=-30)
        response = self.client.get(reverse('index'))
        self.assertQuerysetEqual(
            response.context['vehicle_list'],
            ['<Vehicle: Past Vehicle released on: 2020-09-22>']
        )
    def test_future_question(self):
        create_vehicle(vehicle_type="Future Vehicle", days=30)
        response = self.client.get(reverse('index'))
        self.assertQuerysetEqual(response.context['vehicle_list'], ['<Vehicle: Future Vehicle released on: 2020-11-21>'])

    def test_no_questions(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

        self.assertQuerysetEqual(response.context['vehicle_list'], [])