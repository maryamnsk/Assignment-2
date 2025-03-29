# Import the Room class from the Room_Invoice_Payment file
from Room_Invoice_Payment import Room


# Define a test function for searching available rooms
def search_available_rooms_test():
    """Test case for searching available rooms based on user input criteria"""

    # show the purpose of this test case
    print("Testing Room Search functionality")

    try:
        # ask the user to enter the desired room type and standardize the input
        room_type = input("Enter the room type (Single, Double, Suite): ").strip().capitalize()

        # Validate if the entered room type is correct
        if room_type not in ["Single", "Double", "Suite"]:
            raise ValueError("Invalid room type entered. Please enter Single, Double, or Suite.")

        # ask the the user to enter the check-in and check-out dates
        check_in_date = input("Enter check-in date (YYYY-MM-DD): ").strip()
        check_out_date = input("Enter check-out date (YYYY-MM-DD): ").strip()

        #validation to check if the date format is correct (should contain two hyphens)
        if not (check_in_date.count('-') == 2 and check_out_date.count('-') == 2):
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

        # ask the the user to enter required amenities (comma-separated) or press Enter for none
        amenities_input = input("Enter amenities (separate by commas, or press Enter for none): ").strip()

        #Convert the comma-separated string into a list of amenities, removing extra spaces
        if amenities_input:
            amenities = [item.strip() for item in amenities_input.split(",")]
        else:
            amenities = []  #If the user presses Enter, an empty list is used

        #Create a list of Room objects to simulate available rooms in the hotel
        rooms = [
            Room(101, "Single", 100, True, ["WiFi", "TV"]),  # Available Single room with WiFi & TV
            Room(102, "Suite", 250, False, ["WiFi", "TV", "Mini Bar"]),  # Unavailable Suite with amenities
            Room(103, "Double", 150, True, ["WiFi", "Mini Bar"]),  # Available Double room with WiFi & Mini Bar
            Room(104, "Single", 120, True, ["WiFi", "TV"]),  # Available Single room with WiFi & TV
        ]

        #create an empty list to store rooms that match the user's criteria
        available_rooms = []

        # loop through each room in the list to check if it matches the search criteria
        for room in rooms:
            # Check if the room type matches the user's input and if it is available
            if room.get_room_type() == room_type and room.get_availability_status():
                # Check if the room contains all the requested amenities
                if all(amenity in room.get_amenities() for amenity in amenities):
                    available_rooms.append(room)  # Add the room to the available list

        #Check if there are available rooms matching the search criteria
        if available_rooms:
            # Display the list of available rooms
            print("\nAvailable Rooms:")
            for room in available_rooms:
                print(room)  # Print room details using the `__str__` method from the Room class
        else:
            #Display a message if no rooms match the search criteria
            print("No available rooms match your criteria.")

    # Handle invalid room type or date format errors
    except ValueError as ve:
        print("Error:", ve)

    # Handle any other unexpected errors
    except Exception as e:
        print("An unexpected error occurred:", e)


# Run the test case function
search_available_rooms_test()
