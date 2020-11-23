from django.test import TestCase

from main.models import Destination


class DestinationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Destination.objects.create(destination_id=1,
                                   state="New South Wales",
                                   stateCode="NSW",
                                   name="Sydney",
                                   description="noice place",
                                   image="abcd",
                                   likes=1,
                                   dislikes=1,
                                   click_count=1,
                                   userLike="",
                                   userDislike="")

    def test_state_label(self):
        destination = Destination.objects.get(destination_id=1)
        field_label = destination._meta.get_field('state').verbose_name
        self.assertEqual(field_label, 'New South Wales')

    def test_state_max_length(self):
        destination = Destination.objects.get(destination_id=1)
        max_length = destination._meta.get_field('state').max_length
        self.assertEqual(max_length, 30)

    def test_state_code_label(self):
        destination = Destination.objects.get(destination_id=1)
        field_label = destination._meta.get_field('stateCode').verbose_name
        self.assertEqual(field_label, 'NSW')

    def test_state_code_max_length(self):
        destination = Destination.objects.get(destination_id=1)
        max_length = destination._meta.get_field('stateCode').max_length
        self.assertEqual(max_length, 10)

    def test_name_label(self):
        destination = Destination.objects.get(destination_id=1)
        field_label = destination._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Sydney')

    def test_name_max_length(self):
        destination = Destination.objects.get(destination_id=1)
        max_length = destination._meta.get_field('name').max_length
        self.assertEqual(max_length, 30)

    def test_description_label(self):
        destination = Destination.objects.get(destination_id=1)
        field_label = destination._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'noice place')

