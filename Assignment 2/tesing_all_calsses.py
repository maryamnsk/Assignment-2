# Import the classes from the other files
from Guest_Hotel_ServiceRequest import (Guest, Hotel, ServiceRequest)
from Booking_Feedback_Staff import (Booking, Feedback, Staff)
from Room_Invoice_Payment import (Room, Invoice, Payment)

def test_all_classes():
#tesing all the classes together
    try:
        #Create a Hotel object with name, location, and number of rooms
        hotel = Hotel("Royal Stay", "Dubai", 100)
        #Print the hotel details using string concatenation
        print("Hotel Created: " + str(hotel))

        #Create two Room objects with room number, type, price, and availability
        room1 = Room("101", "Single", 100.0, True)
        room2 = Room("102", "Double", 150.0, True)

        #Add the rooms to the hotel
        hotel.add_room(room1)
        hotel.add_room(room2)

        #Print the list of rooms added using string conversion and concatenation
        print("Rooms Added to Hotel: " + str([room1, room2]))

        #Create a Guest object (initially with no details)
        guest = Guest()

        #Collect guest details from user input
        guest.collect_details()

        #Set loyalty points for the guest
        guest.set_loyalty_points(50)

        #Print the guest details using string concatenation
        print("Guest Details: " + str(guest))

        #Create a Booking object with booking ID, check-in and check-out dates, and status
        booking = Booking("B001", "2025-03-28", "2025-03-30", "Confirmed")

        #Mark room1 as unavailable (since it is booked)
        room1.set_availability_status(False)

        #Print booking details using string concatenation
        print("Booking Created: " + str(booking))

        #Create an Invoice object with total amount, discount, and payment status
        invoice = Invoice(200.0, discounts=20.0, payment_status="Unpaid")

        #Print invoice details using string concatenation
        print("Invoice Generated: " + str(invoice))

        #Create a Payment object with payment ID, amount, and payment method
        payment = Payment("P001", 180.0, "Credit Card")

        #Print payment details using string concatenation
        print("Payment Processed: " + str(payment))

        #Create a ServiceRequest object with request ID, service type, and status
        service_request = ServiceRequest("SR001", "Housekeeping", "Pending")

        #Update the service request status to "Completed"
        service_request.set_status("Completed")

        #Print service request details using string concatenation
        print("Service Request: " + str(service_request))

        #Create a Feedback object with rating, comments, and timestamp
        feedback = Feedback(5, "Excellent stay! Great service.", "2025-03-31")

        #Print feedback details using string concatenation
        print("Feedback Submitted: " + str(feedback))

    #Handle any exceptions that may occur during execution
    except Exception as e:
        #Print an error message using string concatenation
        print("An error occurred during the test: " + str(e))

#Run the test function if this script is executed as the main program
if __name__ == "__main__":
    test_all_classes()
