from reservation_system import Hotel, Customer, Reservation
import uuid


print("\n--- Hotel Management Testing ---\n")

# Create and define a hotel
hotel = Hotel("Grand Plaza", "New York", 50)
print("\nDefining hotel...")
hotel.define_hotel()

# Display hotel info
print("\nDisplaying hotel information:")
hotel.display_hotel_info()

# Modify hotel details
print("\nModifying hotel information...")
hotel.modify_hotel("Guadalajara", 100, 100)
hotel.display_hotel_info()

# Booking a room
print("\nBooking a room...")
hotel.book_room()
hotel.display_hotel_info()

# Canceling a booking
print("\nCanceling a booking...")
hotel.cancel_book()
hotel.display_hotel_info()

# Deleting the hotel 
# print("\nDeleting the hotel...")
# hotel.delete_hotel()
# hotel.display_hotel_info()


print("\n--- Customer Management Testing ---\n")

# Create customers
customer_1 = Customer("Juan", "123453")
print("\nCreating customer Juan...")
customer_1.create_customer()

customer_2 = Customer("Luis", "492843")
print("\nCreating customer Luis...")
customer_2.create_customer()

# Retrieve customer information 
customer_id = "f55c0c64-eed6-4b2e-8b4d-8e79d775f1d8"
print(f"\nRetrieving customer info for ID: {customer_id}")
customer_1.customer_info(customer_id)

# Editing customer info
print("\nEditing customer info...")
customer_1.edit_customer_info(customer_id, new_name="Juan Carlos")

# Deleting a customer 
# print("\nDeleting customer Juan...")
# customer_1.delete_customer(customer_id)


print("\n--- Reservation Management Testing ---\n")

# Create a reservation
reservation_1 = Reservation("Ron", "Holiday", 2)
print("\nCreating reservation...")
reservation_1.create_reservation()

# Cancel reservation 
reservation_id = "76ac739b-d417-4afe-a14e-997a62aaa334"
print(f"\nCanceling reservation with ID: {reservation_id}")
reservation_1.cancel_reservation(reservation_id)

print("\n--- Manual Testing Completed ---\n")
