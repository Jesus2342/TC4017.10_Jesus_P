"""Necessary modules to hanlde Json saving/loading and to create unique IDs"""
import uuid
from random import randint
from json_handler import load_json, save_json

HOTEL_FILE = "h_rec.json"
CUSTOMER_FILE = "cust_rec.json"
RESERVATION_FILE = "reservation_record.json"


class Hotel:
    """Represents a hotel with attributes and methods"""

    def __init__(self, h_name, hotel_loc, n_rooms):
        """Initializes a hotel with name, location, and number of rooms."""
        if not h_name or not isinstance(h_name, str):
            raise ValueError("Hotel name must be a non-empty string.")
        if not hotel_loc or not isinstance(hotel_loc, str):
            raise ValueError("Hotel location must be a non-empty string.")
        if not isinstance(n_rooms, int) or n_rooms <= 0:
            raise ValueError("Number of rooms must be a positive integer.")

        self.h_name = h_name
        self.hotel_loc = hotel_loc
        self.n_rooms = n_rooms
        self.availability_rooms = n_rooms
        self.h_rec = load_json(HOTEL_FILE)

    def save_hotel_record(self):
        """Saves hotel records to a JSON file."""
        save_json(HOTEL_FILE, self.h_rec)

    def define_hotel(self):
        """Defines and saves hotel data to JSON."""
        self.h_rec[self.h_name] = {
            "location": self.hotel_loc,
            "n_rooms": self.n_rooms,
            "free_rooms": self.availability_rooms,
        }
        self.save_hotel_record()

    def delete_hotel(self):
        """Deletes the hotel from records."""
        if self.h_name in self.h_rec:
            del self.h_rec[self.h_name]
            self.save_hotel_record()

    def display_hotel_info(self):
        """Displays hotel details."""
        print(f"Details: {self.h_rec.get(self.h_name, 'Hotel not found')}")

    def modify_hotel(
        self, new_location=None, new_num_rooms=None, new_available_rooms=None
    ):
        """Modifies hotel details such as location and room availability."""
        if self.h_name in self.h_rec:
            if new_location:
                self.h_rec[self.h_name]["location"] = new_location
            if new_num_rooms is not None:
                self.h_rec[self.h_name]["n_rooms"] = new_num_rooms
            if new_available_rooms is not None:
                self.h_rec[self.h_name]["free_rooms"] = new_available_rooms
            self.save_hotel_record()
            print(f"Hotel {self.h_name} updated successfully.")
        else:
            print("Hotel not found.")

    def book_room(self):
        """Books a room if available."""
        if self.h_name in self.h_rec:
            if self.h_rec[self.h_name]["free_rooms"] > 0:
                self.h_rec[self.h_name]["free_rooms"] -= 1
                self.save_hotel_record()
                print("Room booked successfully!")
            else:
                print("No rooms available at this time.")
        else:
            print("Hotel not found.")

    def cancel_book(self):
        """Cancels a room booking if applicable."""
        if self.h_name in self.h_rec:
            if (
                self.h_rec[self.h_name]["free_rooms"]
                < self.h_rec[self.h_name]["n_rooms"]
            ):
                self.h_rec[self.h_name]["free_rooms"] += 1
                self.save_hotel_record()
                print("Booking canceled successfully!")
            else:
                print("No active reservations.")
        else:
            print("Hotel not found.")


class Customer:
    """Represents a customer with methods to manage customer records."""

    def __init__(self, cus_name, customer_phone):
        """Initializes a customer with name and phone number."""
        if not cus_name or not isinstance(cus_name, str):
            raise ValueError("Customer name must be a non-empty string.")
        if not isinstance(customer_phone, int) or customer_phone <= 0:
            raise ValueError("Phone must be a positive integer.")

        self.cus_name = cus_name
        self.customer_phone = customer_phone
        self.cust_rec = load_json(CUSTOMER_FILE)

    def save_customer_record(self):
        """Saves customer records to a JSON file."""
        save_json(CUSTOMER_FILE, self.cust_rec)

    def create_customer(self):
        """Creates a new customer and assigns a unique ID."""
        cust_id = str(uuid.uuid4())
        self.cust_rec[cust_id] = {
            "name": self.cus_name,
            "phone": self.customer_phone,
            "customer_room": randint(1, 100),
        }
        print(
            f"Customer {self.cus_name} created successfully with ID {cust_id}"
        )
        self.save_customer_record()

    def customer_info(self, cust_id):
        """Retrieves customer details using their unique ID."""
        print(
            f"Details: {self.cust_rec.get(cust_id, 'Customer not found')}"
        )

    def delete_customer(self, cust_id):
        """Deletes a customer by their ID."""
        if cust_id in self.cust_rec:
            del self.cust_rec[cust_id]
            self.save_customer_record()
            print(f"Customer {cust_id} deleted successfully.")
        else:
            print("Customer not found.")

    def edit_customer_info(self, cust_id, new_name=None, new_phone=None):
        """Edits a customer's information."""
        if cust_id in self.cust_rec:
            if new_name:
                self.cust_rec[cust_id]["name"] = new_name
            if new_phone:
                self.cust_rec[cust_id]["phone"] = new_phone
            self.save_customer_record()
            print(f"Customer {cust_id} updated successfully.")
        else:
            print("Customer not found.")


class Reservation:
    """Represents a reservation with methods to manage bookings."""

    def __init__(self, cus_name, h_name, num_days):
        """Initializes a reservation"""
        self.cus_name = cus_name
        self.h_name = h_name
        self.num_days = num_days
        self.reservation_record = load_json(RESERVATION_FILE)

    def save_reservation_record(self):
        """Saves reservation records to a JSON file."""
        save_json(RESERVATION_FILE, self.reservation_record)

    def create_reservation(self):
        """Creates a reservation and assigns a unique ID."""
        reservation_id = str(uuid.uuid4())
        self.reservation_record[reservation_id] = {
            "name": self.cus_name,
            "hotel": self.h_name,
            "num_days": self.num_days,
        }
        print(
            f"Reservation created for {self.cus_name} with ID {reservation_id}"
        )
        self.save_reservation_record()

    def cancel_reservation(self, reservation_id):
        """Cancels a reservation by its ID."""
        if reservation_id in self.reservation_record:
            del self.reservation_record[reservation_id]
            self.save_reservation_record()
            print("Reservation was deleted successfully.")
        else:
            print("Reservation was not found.")
