# Import the Booking class from the Booking_Feedback_Staff file
from Booking_Feedback_Staff import Booking


#a function to test booking confirmation and cancellation
def test_booking_confirmation():
    try:
        # Test: Booking confirmation
        print("Booking Confirmation Test")

        # ask the user to input booking details
        booking_id = int(input("Enter booking ID: "))  # Ask the user for and convert the booking ID to an integer
        check_in_date = input("Enter check-in date: ")  # Ask the user for check-in date input
        check_out_date = input("Enter check-out date: ")  # Ask the user for check-out date input

        #Create a Booking object with the provided input details
        booking = Booking(booking_id, check_in_date, check_out_date)

        #Set the status of the booking to 'Confirmed'
        booking.set_status("Confirmed")

        #Print the booking confirmation message
        print("Booking Confirmed: " + str(booking))  #Convert the booking object to string and concatenate it for printing

        # Test: Booking cancellation
        cancel = input(
            "Do you want to cancel the booking? (yes/no): ").lower()  # Ask the user if s/he wants to cancel the booking
        if cancel == "yes":  # If the user answers 'yes', cancel the booking
            booking.set_status("Canceled")  # Change the booking status to 'Canceled'

            #Print the booking cancellation message
            print("Booking Canceled: " + str(booking))  #Convert the booking object to string and concatenate it for printing

    # Catch specific ValueError if the user enters invalid data (e.g., non-integer booking ID)
    except ValueError as e:
        print("ValueError in Booking Confirmation Test Case: " + str(e))  # Print an error message for ValueError

    # Catch any other exceptions and print an error message
    except Exception as e:
        print("Error in Booking Confirmation Test Case: " + str(e))  # Print a generic error message for any other exceptions



if __name__ == "__main__":
    test_booking_confirmation()