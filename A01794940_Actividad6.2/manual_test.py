from reservation_system import Hotel

# Create a new hotel instance
hotel = Hotel("Grand Plaza", "New York", 50)

# Define the hotel (adds it to the JSON file)
hotel.define_hotel()

# Show available rooms
hotel.show_free_rooms()

# Book a room
hotel.book_room()

# Cancel a booking
hotel.cancel_book()

# Delete the hotel
hotel.delete_hotel()
