from json_handler import load_json, save_json

HOTEL_FILE = "hotels.json"

class Hotel:
    def __init__(self, hotel_name, hotel_loc, num_rooms):
        self.hotel_name = hotel_name
        self.hotel_loc = hotel_loc
        self.num_rooms = num_rooms
        self.availability_rooms = num_rooms  # Initially, all rooms are available

    def define_hotel(self):
        """Save hotel data to JSON"""
        
        hotels = load_json(HOTEL_FILE)
        hotels[self.hotel_name] = {
            "location": self.hotel_loc,
            "num_rooms": self.num_rooms,
            "available_rooms": self.availability_rooms
        }
        
        save_json(HOTEL_FILE, hotels)

    def delete_hotel(self):
        hotels = load_json(HOTEL_FILE)
        
        if self.hotel_name in hotels:
            del hotels[self.hotel_name]
            save_json(HOTEL_FILE, hotels)

    def show_free_rooms(self):
        hotels = load_json(HOTEL_FILE)
        
        if self.hotel_name in hotels:
            print(f"Number of rooms avaialble is: {hotels[self.hotel_name]['available_rooms']}")
            
        else:
            print("The Hotel was not found")
        
        



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

