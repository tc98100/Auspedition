from django.test import TestCase
from .models import *

class DestinationTestCase(TestCase):
    def setUpTestData(cls):
        Destination.objects.create(destination_id='Ballarat-VIC', state='Victoria', stateCode='VIC', name='Ballarat',
                                   description='nice city', image='image.png', likes=0, dislikes=0, click_count=0)

    def test_labels(self):
        city = Destination.objects.get(destination_id='Ballarat-VIC')
        label = city._meta.get_field('state').verbose_name
        self.assertEqual(label, 'state')
