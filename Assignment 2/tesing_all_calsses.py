# Import all the classes from the files
from Guest_Hotel_ServiceRequest import (Guest, Hotel, ServiceRequest)
from Booking_Feedback_Staff import (Booking, Feedback, Staff)
from Room_Invoice_Payment import (Room, Invoice, Payment)


# 1.Guest Account Creation Test Case
def test_guest_account_creation():
    #Test the process of guest account creation with user input
    try:
        for i in range(2):  #Run the test twice for different guests
            print("\nTest Case", i + 1, ": Guest Account Creation")

            #get the guest details from user input
            name = input("Enter guest name: ")
            email = input("Enter guest email: ")
            contact = input("Enter guest contact number: ")

            #Create a new Guest object with the input data
            guest = Guest(name, email, contact)

            #Display confirmation message
            print("Guest account created successfully:", guest)

    except ValueError:
        #Handle case where user enters incorrect data type
        print("Invalid input! Please enter correct values.")

    except Exception as e:
        #Handle any unexpected errors
        print("Error in Guest Account Creation Test Case:", e)


# 2. Searching for Available Rooms Test Case
def test_searching_for_available_rooms():
    #Test searching for available rooms based on user input
    try:
        #Create a new hotel object
        hotel = Hotel("Royal Stay", "Paris", 10)

        #rooms in the hotel
        hotel.add_room(Room(101, "Single", 100))  # Available room
        hotel.add_room(Room(102, "Suite", 250, False))  # Unavailable room
        hotel.add_room(Room(103, "Double", 150))  # Available room

        for i in range(2):  # Run two test cases
            print("\nTest Case", i + 1, ": Searching for Available Rooms")

            # Ask the user for the desired room type
            room_type = input("Enter the room type (Single, Double, Suite): ")

            # Find available rooms matching the input room type
            available_rooms = [room for room in hotel._rooms
                               if room.get_availability_status() and room.get_room_type().lower() == room_type.lower()]

            #Display available rooms or a message if none are found
            if available_rooms:
                print("Available Rooms:")
                for room in available_rooms:
                    print(str(room))  #Ensure the room details are displayed properly
            else:
                print("No rooms available for the selected type.")

    except Exception as e:
        # Handle any unexpected errors
        print("Error in Searching for Available Rooms Test Case:", e)


# 3.Making a Room Reservation Test Case
def test_making_a_room_reservation():
    #Test the reservation process with user input
    try:
        for i in range(2):  #Run the test twice
            print("\nTest Case", i + 1, ": Making a Room Reservation")

            #Collect guest details
            name = input("Enter guest name: ")
            email = input("Enter guest email: ")
            contact = input("Enter guest contact: ")

            #Create a new Guest object
            guest = Guest(name, email, contact)

            #Ask the user for room details
            room_number = int(input("Enter room number to book (101, 102, 103): "))
            check_in = input("Enter check-in date (YYYY-MM-DD): ")
            check_out = input("Enter check-out date (YYYY-MM-DD): ")

            #Create a booking object
            booking = Booking(room_number, check_in, check_out)

            #Display confirmation message
            print("Room successfully reserved!", booking)

    except ValueError as ve:
        #Handle cases where user enters incorrect data type
        print("Invalid input:", ve)

    except Exception as e:
        #Handle unexpected errors
        print("Error in Making a Room Reservation Test Case:", e)


# 4.Invoice Generation for a Booking Test Case
def test_invoice_generation_for_booking():
    #Test generating an invoice with user input
    try:
        for i in range(2):  # Run the test twice
            print("\nTest Case", i + 1, ": Invoice Generation")

            #Collect invoice details from user
            total_amount = float(input("Enter total amount: "))
            discounts = float(input("Enter discount amount (if any): "))

            #Create an Invoice object
            invoice = Invoice(total_amount, discounts)

            #Display the generated invoice
            print("Invoice Generated:", invoice)

    except ValueError:
        #Handle invalid numerical input
        print("Invalid input! Please enter valid numbers for amounts.")

    except Exception as e:
        #Handle unexpected errors
        print("Error in Invoice Generation Test Case:", e)


# 5. Processing Different Payment Methods Test Case
def test_processing_payment_methods():
    #Test different payment methods
    try:
        for i in range(2):  #Run the test twice
            print("\nTest Case", i + 1, ": Processing Payment")

            #Collect payment details from user
            payment_id = int(input("Enter payment ID: "))
            amount = float(input("Enter payment amount: "))
            method = input("Enter payment method (Credit Card, Debit Card, Mobile Wallet): ")

            #Create a Payment object
            payment = Payment(payment_id, amount, method)

            #Display confirmation message
            print("Payment Processed:", payment)

    except ValueError:
        #Handle invalid input
        print("Invalid input! Payment ID must be a number.")

    except Exception as e:
        #Handle unexpected errors
        print("Error in Payment Processing Test Case:", e)


# 6.Displaying Reservation History Test Case
def test_displaying_reservation_history():
    #Test displaying a guest's reservation history
    try:
        for i in range(2):  # Run the test twice
            print("\nTest Case", i + 1, ": Displaying Reservation History")

            #Collect the guest and booking details
            guest_name = input("Enter guest name: ")
            booking_id = int(input("Enter booking ID: "))
            check_in = input("Enter check-in date: ")
            check_out = input("Enter check-out date: ")

            #Create a booking object
            booking = Booking(booking_id, check_in, check_out)

            #Display reservation history
            print("Reservation history for", guest_name, ":", booking)

    except ValueError:
        #Handle incorrect numerical input
        print("Invalid input! Booking ID must be a number.")

    except Exception as e:
        #Handle unexpected errors
        print("Error in Reservation History Test Case:", e)


# 7.Cancellation of a Reservation Test Case
def test_cancellation_of_reservation():
    #Test canceling a reservation
    try:
        for i in range(2):  # Run the test twice
            print("\nTest Case", i + 1, ": Cancelling a Reservation")

            #get the booking details
            booking_id = int(input("Enter booking ID: "))
            check_in = input("Enter check-in date: ")
            check_out = input("Enter check-out date: ")

            #Create a booking object
            booking = Booking(booking_id, check_in, check_out)

            #Cancel the booking
            booking.set_status("Canceled")

            #Display confirmation message
            print("Reservation Canceled:", booking)

    except ValueError:
        #Handle invalid input
        print("Invalid input! Booking ID must be a number.")

    except Exception as e:
        #Handle unexpected errors
        print("Error in Reservation Cancellation Test Case:", e)


# Run all test cases
if __name__ == "__main__":
    test_guest_account_creation()
    test_searching_for_available_rooms()
    test_making_a_room_reservation()
    test_invoice_generation_for_booking()
    test_processing_payment_methods()
    test_displaying_reservation_history()
    test_cancellation_of_reservation()