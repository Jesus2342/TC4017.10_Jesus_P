"""Importing Unit test for testing classes"""
import unittest
from reservation_system import Hotel, Customer, Reservation

HOTEL_FILE = "h_rec.json"
CUSTOMER_FILE = "cust_rec.json"
RESERVATION_FILE = "reservation_record.json"


class TestHotel(unittest.TestCase):
    """Unit tests for the Hotel class."""

    def setUp(self):
        """Setup a test hotel instance before each test."""
        self.hotel = Hotel("TestHotel", "TestCity", 10)
        self.hotel.define_hotel()

    def tearDown(self):
        """Cleanup after each test."""
        self.hotel.delete_hotel()

    def test_define_hotel(self):
        """Test hotel creation."""
        self.assertIn("TestHotel", self.hotel.h_rec)

    def test_modify_hotel(self):
        """Test modifying hotel details."""
        self.hotel.modify_hotel(new_location="NewCity", new_num_rooms=20)
        self.assertEqual(self.hotel.h_rec["TestHotel"]["location"], "NewCity")

    def test_book_room(self):
        """Test booking a room."""
        initial_rooms = self.hotel.h_rec["TestHotel"]["free_rooms"]
        self.hotel.book_room()
        self.assertEqual(
            self.hotel.h_rec["TestHotel"]["free_rooms"],
            initial_rooms - 1)

    def test_cancel_booking(self):
        """Test canceling a booking."""
        self.hotel.book_room()
        initial_rooms = self.hotel.h_rec["TestHotel"]["free_rooms"]
        self.hotel.cancel_book()
        self.assertEqual(
            self.hotel.h_rec["TestHotel"]["free_rooms"],
            initial_rooms + 1)


class TestCustomer(unittest.TestCase):
    """Unit tests for the Customer class."""

    def setUp(self):
        """Setup a test customer instance before each test."""
        self.customer = Customer("John Doe", 1234567890)
        self.customer.create_customer()
        self.customer_id = list(self.customer.cust_rec.keys())[0]

    def tearDown(self):
        """Cleanup after each test."""
        self.customer.delete_customer(self.customer_id)

    def test_create_customer(self):
        """Test customer creation."""
        self.assertIn(self.customer_id, self.customer.cust_rec)

    def test_edit_customer_info(self):
        """Test editing customer details."""
        self.customer.edit_customer_info(
            self.customer_id, new_name="Julia Perez")
        self.assertEqual(
            self.customer.cust_rec[self.customer_id]["name"], "Julia Perez")


class TestReservation(unittest.TestCase):
    """Unit tests for the Reservation class."""

    def setUp(self):
        """Setup a test reservation instance before each test."""
        self.reservation = Reservation("Carlos Lopez", "TestHotel", 3)
        self.reservation.create_reservation()
        self.reservation_id = list(
            self.reservation.reservation_record.keys())[0]

    def tearDown(self):
        """Cleanup after each test."""
        self.reservation.cancel_reservation(self.reservation_id)

    def test_create_reservation(self):
        """Test reservation creation."""
        self.assertIn(self.reservation_id, self.reservation.reservation_record)

    def test_cancel_reservation(self):
        """Test canceling a reservation."""
        self.reservation.cancel_reservation(self.reservation_id)
        self.assertNotIn(
            self.reservation_id,
            self.reservation.reservation_record)


class TestNegativeCases(unittest.TestCase):
    """Negative test cases to verify error handling in the system."""

    def test_create_hotel_with_invalid_data(self):
        """Test creating a hotel with invalid inputs."""
        with self.assertRaises(ValueError):
            Hotel("", "New York", 50)
        with self.assertRaises(ValueError):
            Hotel("Grand Plaza", "", 50)
        with self.assertRaises(ValueError):
            Hotel("Grand Plaza", "New York", -10)

    def test_create_customer_with_invalid_data(self):
        """Test creating a customer with invalid inputs."""
        with self.assertRaises(ValueError):
            Customer("", 1234567890)
        with self.assertRaises(ValueError):
            Customer("Juan", "phone_number")

    def test_reservation_for_non_existent_hotel(self):
        """Test making a reservation at a non-existent hotel."""
        reservation = Reservation("Juan", "Fake Hotel", 3)
        reservation.create_reservation()

    def test_booking_room_in_non_existent_hotel(self):
        """Test booking a room in a hotel that does not exist."""
        hotel = Hotel("Non Existent Hotel", "Nowhere", 10)
        hotel.h_rec = {}
        hotel.book_room()

    def test_cancel_non_existent_reservation(self):
        """Test canceling a reservation that does not exist."""
        reservation = Reservation("Luis", "Grand Plaza", 2)
        reservation.cancel_reservation("non-existent-id")


if __name__ == "__main__":
    unittest.main()
