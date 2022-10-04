# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from datetime import date
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Table, Booking, User
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# These test will create a new food and drink item,
# it will check the name, description and price


class TestModels(TestCase):

    def setUp(self):
        self.table = Table(table_id=1, table_name='Outdoor 1', max_seats=6)
        self.user = User(
            username='Tester Test',
            email='test@aaa.com'
            )
        self.booking = Booking(
            booking_id=32,
            table=self.table,
            user=self.user,
            guest_count=6,
            created_date='2022-12-12',
            requested_date='2022-12-12',
            requested_time='12:00',
            status='awaiting confirmation',
            name='Tester Test',
            phone='+353123456789',
            email='test@aaa.com',
            )

    def test_create_booking(self):
        self.assertEqual(self.booking.name, 'Tester Test')
        self.assertEqual(self.booking.booking_id, 32)
        self.assertEqual(self.booking.requested_date, '2022-12-12')
        self.assertEqual(self.booking.requested_time, '12:00')
        self.assertEqual(self.booking.guest_count, 6)
        self.assertEqual(self.booking.status, 'awaiting confirmation')
        self.assertEqual(self.booking.name, 'Tester Test')
        self.assertEqual(self.booking.phone, '+353123456789')
        self.assertEqual(self.booking.email, 'test@aaa.com')
