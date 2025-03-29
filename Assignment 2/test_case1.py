# Import the Guest class from the Guest_Hotel_ServiceRequest file
from Guest_Hotel_ServiceRequest import Guest

#a function to test guest account creation
def test_guest_account_creation():
    try:
        # Test 1: Creating a new guest account
        print("Test 1: Creating a new guest account") 
        name = input("Enter guest name: ")  # ask the user to enter guest name
        email = input("Enter guest email: ")  # ask the user to enter guest email
        loyalty_points = int(
            input("Enter loyalty points: "))  # ask the user for loyalty points, and change the input into integer

        #Create a new Guest object using the provided inputs
        guest1 = Guest(name, email, loyalty_points)

        #Print the guest account creation message
        print("Guest Account Created: " + str(guest1))

        # Test 2: Creating another guest account
        print("\nTest 2: Creating another guest account") 
        name = input("Enter guest name: ")  # ask the user to enter another guest name
        email = input("Enter guest email: ")  # ask the user to enter another guest email
        loyalty_points = int(
            input("Enter loyalty points: "))  # ask the user for loyalty points, and change the input into integer

        #Create another Guest object using the new inputs
        guest2 = Guest(name, email, loyalty_points)

        #Print the second guest account creation message
        print("Guest Account Created: " + str(guest2))  # Convert guest2 object to string and print

    # this will handle specific ValueError exceptions (if user inputs invalid data)
    except ValueError as e:
        print("ValueError in Guest Account Creation: " + str(e))  #Print the error message if ValueError occurs

    #General exception handling for other types of errors
    except Exception as e:
        print("Error in Guest Account Creation Test Case: " + str(e))  #Print generic error message for any other exceptions


if __name__ == "__main__":
    test_guest_account_creation()