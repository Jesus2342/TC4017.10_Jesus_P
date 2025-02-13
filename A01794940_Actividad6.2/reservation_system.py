from json_handler import load_json, save_json
import uuid
from random import randint
HOTEL_FILE = "hotel_record.json"

class Hotel:
    def __init__(self, hotel_name, hotel_loc, num_rooms):
        self.hotel_name = hotel_name
        self.hotel_loc = hotel_loc
        self.num_rooms = num_rooms
        self.availability_rooms = num_rooms
        self.hotel_record = load_json(HOTEL_FILE)  

    def save_hotel_record(self):
        save_json(HOTEL_FILE, self.hotel_record)  

    def define_hotel(self):
        """Save hotel data to JSON"""
        self.hotel_record[self.hotel_name] = {  
            "location": self.hotel_loc,
            "num_rooms": self.num_rooms,
            "available_rooms": self.availability_rooms,
        }
        self.save_hotel_record()

    def delete_hotel(self):
        if self.hotel_name in self.hotel_record:  
            del self.hotel_record[self.hotel_name]
            self.save_hotel_record()

    def display_hotel_info(self): 
        print(f"Hotel details: {self.hotel_record[self.hotel_name]}")
        
    def modify_hotel(self, new_location=None, new_num_rooms=None, new_available_rooms=None):
        self.hotel_record[self.hotel_name]["location"] = new_location
        self.hotel_record[self.hotel_name]["num_rooms"] = new_num_rooms
        self.hotel_record[self.hotel_name]["available_rooms"] = new_available_rooms
        self.save_hotel_record()
        print(f"Hotel {self.hotel_name} updated successfully.")

    def book_room(self):
        if self.hotel_name in self.hotel_record:  
            if self.hotel_record[self.hotel_name]["available_rooms"] > 0:
                self.hotel_record[self.hotel_name]["available_rooms"] -= 1
                self.save_hotel_record()
                print("Room booked successfully!")
            else:
                print("No rooms available at this time")
        else:
            print("Hotel not found")

    def cancel_book(self):
        if self.hotel_name in self.hotel_record: 
            if self.hotel_record[self.hotel_name]["available_rooms"] < self.hotel_record[self.hotel_name]["num_rooms"]:
                self.hotel_record[self.hotel_name]["available_rooms"] += 1
                self.save_hotel_record()
                print("Booking canceled successfully!")
            else:
                print("No active reservations")
        else:
            print("Hotel not found")



CUSTOMER_FILE = "customer_record.json"

class Customer:
    def __init__(self, customer_name, customer_phone):
        self.customer_name = customer_name
        self.customer_phone = customer_phone
        self.customer_record = load_json(CUSTOMER_FILE)

    def save_customer_record(self):
        save_json(CUSTOMER_FILE, self.customer_record)

    def create_customer(self):
        """Creates a new customer and assigns a unique ID."""
        customer_id = str(uuid.uuid4())  
        self.customer_record[customer_id] = {
            "name": self.customer_name,
            "phone": self.customer_phone,
            "customer_room": randint(1, 100),
        }
        print(f"Customer {self.customer_name} created successfully with ID {customer_id}")
        self.save_customer_record()

    def customer_info(self, customer_id):
        """Retrieves customer details using their unique ID."""
        if customer_id in self.customer_record:
            print(f"Customer details: {self.customer_record[customer_id]}")
        else:
            print("Customer not found.")

    def delete_customer(self, customer_id):
        """Deletes a customer by their ID."""
        if customer_id in self.customer_record:
            del self.customer_record[customer_id]
            self.save_customer_record()
            print(f"Customer {customer_id} deleted successfully.")
        else:
            print("Customer not found.")

    def edit_customer_info(self, customer_id, new_name=None, new_phone=None):
        """Edits a customer's information."""
        if customer_id in self.customer_record:
            if new_name:
                self.customer_record[customer_id]["name"] = new_name
            if new_phone:
                self.customer_record[customer_id]["phone"] = new_phone

            self.save_customer_record()
            print(f"Customer {customer_id} updated successfully.")
        else:
            print("Customer not found.")


class Reservation:
    def __init__(self, book_number, customer_name, hotel_name):
        
        self.book_number = book_number
        self.customer_name = customer_name
        self.hotel_name = hotel_name

    def create_reservation(self):
        """Create a new reservation."""
        pass

    def cancel_reservation(self):
        """Cancel a reservation."""
        pass

