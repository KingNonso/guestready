from django.template import Context, Template
from django.test import TestCase

from rental.models import Reservation, Rental


class ReservationTestCase(TestCase):
    fixtures = ['rentals.json']

    def setUp(self):
        rent = Rental.objects.create(name="Res-Test")
        Reservation.objects.create(rent=rent, rental_id="Res-Test-1", checkin="2022-11-11", checkout="2022-11-12")

    def test_model_objects_are_created(self):
        """This test ensures that the model objects are created correctly."""
        rental = Rental.objects.get(name="Res-Test")
        reservation = Reservation.objects.get(rental_id="Res-Test-1")
        self.assertEqual(rental.name, 'Res-Test')
        self.assertEqual(reservation.rental_id, "Res-Test-1")

    def test_fixtures_get_loaded(self):
        """This test ensures that the fixtures are loaded correctly."""
        self.assertEqual(Reservation.objects.count(), 6)

    def test_custom_parent_template_tag(self):
        """This loads and renders the custom template tag 'parent' from previous_reservation.py
        and test it against the expected output, that it works for one case."""
        reservations = Reservation.objects.all()
        out = Template(
            "{% load previous_reservation %} "
            "{% for reservation in reservations %}"
            "{{ reservation|parent }},"
            "{% endfor %}"
        ).render(Context({'reservations': reservations}))
        self.assertIn('Res-1', out)

    def test_call_view_index_page_load(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rental/index.html')

    def test_checkin_checkout_constraint(self):
        """This test ensures that the checkin_lte_checkout constraint is working.
        Checkin date must be less than or equal to checkout date."""
        rent = Rental.objects.create(name="Res-Test")
        with self.assertRaises(Exception):
            Reservation.objects.create(rent=rent, rental_id="Res-Test-1", checkin="2022-11-12", checkout="2022-11-11")


