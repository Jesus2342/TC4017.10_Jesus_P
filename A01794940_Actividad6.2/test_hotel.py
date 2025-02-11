import unittest
import os
import json
from reservation_system import Hotel
from json_handler import load_json, save_json

HOTEL_FILE = "hotels.json"

class TestHotel(unittest.TestCase):

    def setUp(self):
        """Setup a clean hotels.json before each test."""
        self.test_hotel = Hotel("Test Hotel", "Test City", 50)
        save_json(HOTEL_FILE, {})  # Clear file before each test

    def test_define_hotel(self):
        """Test if a hotel is correctly saved in JSON."""
        self.test_hotel.define_hotel()
        hotels = load_json(HOTEL_FILE)
        self.assertIn("Test Hotel", hotels)
        self.assertEqual(hotels["Test Hotel"]["location"], "Test City")

    def test_show_free_rooms(self):
        """Test if the correct number of free rooms is displayed."""
        self.test_hotel.define_hotel()
        hotels = load_json(HOTEL_FILE)
        self.assertIn("Test Hotel", hotels)
        self.assertEqual(hotels["Test Hotel"]["num_rooms"], 50)

    def test_delete_hotel(self):
        """Test hotel deletion from JSON."""
        self.test_hotel.define_hotel()
        self.test_hotel.delete_hotel()
        hotels = load_json(HOTEL_FILE)
        self.assertNotIn("Test Hotel", hotels)

    def tearDown(self):
        """Cleanup test file after each test."""
        if os.path.exists(HOTEL_FILE):
            os.remove(HOTEL_FILE)

if __name__ == "__main__":
    unittest.main()

    
