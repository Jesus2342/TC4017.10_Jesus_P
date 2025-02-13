from reservation_system import Hotel, Customer
import uuid


# Create a new hotel instance
hotel = Hotel("Grand Plaza", "New York", 50)

# Define the hotel (adds it to the JSON file)
hotel.define_hotel()

# Show available rooms
hotel.display_hotel_info()

#Modify Hotel Information 
hotel.modify_hotel("Guadalajara", 100, 100)
hotel.display_hotel_info()

# Book a room
#hotel.book_room()

# Cancel a booking
#hotel.cancel_book()

# Delete the hotel
#hotel.delete_hotel()

"""

customer_1 = Customer("Juan", 123453)
#customer_1.create_customer()


#customer_2 = Customer("Luis", 492843)
#customer_2.create_customer()


customer_1.customer_info("f55c0c64-eed6-4b2e-8b4d-8e79d775f1d8")
"""