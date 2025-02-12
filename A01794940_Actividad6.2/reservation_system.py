from json_handler import load_json, save_json

HOTEL_FILE = "hotel_record.json"

class Hotel:
    def __init__(self, hotel_name, hotel_loc, num_rooms):
        self.hotel_name = hotel_name
        self.hotel_loc = hotel_loc
        self.num_rooms = num_rooms
        self.availability_rooms = num_rooms
        self.hotel_record = load_json(HOTEL_FILE)  

    def save_hotels(self):
        save_json(HOTEL_FILE, self.hotel_record)  

    def define_hotel(self):
        """Save hotel data to JSON"""
        self.hotel_record[self.hotel_name] = {  
            "location": self.hotel_loc,
            "num_rooms": self.num_rooms,
            "available_rooms": self.availability_rooms,
        }
        self.save_hotels()

    def delete_hotel(self):
        if self.hotel_name in self.hotel_record:  
            del self.hotel_record[self.hotel_name]
            self.save_hotels()

    def show_free_rooms(self):
        if self.hotel_name in self.hotel_record:  
            print(f"Number of rooms available: {self.hotel_record[self.hotel_name]['available_rooms']}")
        else:
            print("The hotel was not found")

    def book_room(self):
        if self.hotel_name in self.hotel_record:  
            if self.hotel_record[self.hotel_name]["available_rooms"] > 0:
                self.hotel_record[self.hotel_name]["available_rooms"] -= 1
                self.save_hotels()
                print("Room booked successfully!")
            else:
                print("No rooms available at this time")
        else:
            print("Hotel not found")

    def cancel_book(self):
        if self.hotel_name in self.hotel_record: 
            if self.hotel_record[self.hotel_name]["available_rooms"] < self.hotel_record[self.hotel_name]["num_rooms"]:
                self.hotel_record[self.hotel_name]["available_rooms"] += 1
                self.save_hotels()
                print("Booking canceled successfully!")
            else:
                print("No active reservations")
        else:
            print("Hotel not found")


        
        



class Customer:
    def __init__(self, customer_name, customer_room):
        self.customer_name = customer_name
        self.customer_room = customer_room
        self.customer_reservations = []  

    def create_customer(self):
        """Create a new customer entry."""
        pass

    def delete_customer(self):
        """Delete a customer entry."""
        pass

    def show_customer_info(self):
        """Display customer details."""
        pass

    def edit_customer_info(self, customer_name=None):
        """Modify customer details."""
        pass


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

h1 = Hotel("Grand Plaza", "New York", 100)
h1.define_hotel()

h1.show_free_rooms()

h1.book_room()
h1.show_free_rooms()
