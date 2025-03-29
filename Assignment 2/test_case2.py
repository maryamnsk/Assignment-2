from Room_Invoice_Payment import Room

def search_available_rooms_test():
    print("Testing Room Search functionality")

    try:
        # User input for search criteria
        room_type = input("Enter the room type (Single, Double, Suite): ").strip().capitalize()
        if room_type not in ["Single", "Double", "Suite"]:
            raise ValueError("Invalid room type entered. Please enter Single, Double, or Suite.")

        check_in_date = input("Enter check-in date (YYYY-MM-DD): ").strip()
        check_out_date = input("Enter check-out date (YYYY-MM-DD): ").strip()

        # Input validation for date formats (basic check)
        if not (check_in_date.count('-') == 2 and check_out_date.count('-') == 2):
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

        amenities_input = input("Enter amenities (separate by commas, or press Enter for none): ").strip()
        amenities = [item.strip() for item in amenities_input.split(",")] if amenities_input else []

        # List of rooms to simulate data
        rooms = [
            Room(101, "Single", 100, True, ["WiFi", "TV"]),
            Room(102, "Suite", 250, False, ["WiFi", "TV", "Mini Bar"]),
            Room(103, "Double", 150, True, ["WiFi", "Mini Bar"]),
            Room(104, "Single", 120, True, ["WiFi", "TV"]),
        ]

        available_rooms = []

        # Search available rooms based on criteria
        for room in rooms:
            if room.get_room_type() == room_type and room.get_availability_status():
                # Check for amenities match (all amenities requested must be available)
                if all(amenity in room.get_amenities() for amenity in amenities):
                    available_rooms.append(room)

        # Display available rooms or no results
        if available_rooms:
            print("\nAvailable Rooms:")
            for room in available_rooms:
                print(room)
        else:
            print("No available rooms match your criteria.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the test case
search_available_rooms_test()