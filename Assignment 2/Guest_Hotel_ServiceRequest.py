# Guest Class
class Guest:
    """this class represents the hotel guest with personal information and loyalty points."""
    
    def __init__(self, name=None, contact_info=None, loyalty_points=0):
        #initialize the guest's name as a private attribute
        self.__name = name
        #initialize the guest's contact information as a private attribute
        self.__contact_info = contact_info
        #initialize the guest's loyalty points as a private attribute, defaulting to 0
        self.__loyalty_points = loyalty_points

    #Method to collect guest details if they are new
    def collect_details(self):
        # ask the user to confirm if they are a new guest
        is_new = input("Are you a new guest? (yes/no): ").strip().lower()

        #If the guest is new, get their details
        if is_new == "yes":
            #Ask for the guest's name and store it
            self.__name = input("Enter your Name: ")
            #Ask for the guest's contact information and store it
            self.__contact_info = input("Enter your Contact Information: ")
            #Print a welcome message 
            print("Welcome! Your details have been recorded.")

        #If the guest is not new, then just welcome them
        elif is_new == "no":
            print("Welcome back! Your details are already in the system.")

        #If the user enters an invalid response, show an error message
        else:
            print("Invalid input. Please try again.")

    #getter method to get the guest's name
    def get_name(self):
        return self.__name

    #Setter method to update the guest's name
    def set_name(self, name):
        self.__name = name

    #Getter method to get the guest's contact information
    def get_contact_info(self):
        return self.__contact_info

    #Setter method to update the guest's contact information
    def set_contact_info(self, contact_info):
        self.__contact_info = contact_info

    #Getter method to get the guest's loyalty points
    def get_loyalty_points(self):
        return self.__loyalty_points

    #Setter method to update the guest's loyalty points
    def set_loyalty_points(self, points):
        self.__loyalty_points = points

    #Method to redeem loyalty points
    def redeem_points(self, points):
        #Check if the guest has enough points to redeem
        if points <= self.__loyalty_points:
            #Deduct the redeemed points from the guest's total
            self.__loyalty_points -= points
        else:
            #Raise an error if the guest does not have enough points
            raise ValueError("Not enough loyalty points to redeem.")

    #Method to return a string representation of the Guest object
    def __str__(self):
        # Use string concatenation instead of f-strings to return the guest details
        return "Guest[Name: " + str(self.__name) + ", Contact: " + str(self.__contact_info) + ", Points: " + str(
            self.__loyalty_points) + "]"


# Hotel Class
class Hotel:
    """ a class that represents the hotel, managing rooms, staff, and other operations."""

    def __init__(self, name, location, total_rooms):
        #initialize hotel attributes as protected to allow subclass access
        self._name = name  #Name of the hotel
        self._location = location  #Location of the hotel
        self._total_rooms = total_rooms  #Total number of rooms in the hotel
        self._rooms = []  #List to store Room objects associated with the hotel
        self._staff = []  #List to store Staff objects associated with the hotel

    #method to add a new room to the hotel's room list
    def add_room(self, room):
        self._rooms.append(room)  #Append the room object to the list of rooms.

    #method to add a staff member to the hotel staff list.
    def add_staff(self, staff):
        self._staff.append(staff)  #Append the staff object to the list of staff.

    #Method to return a string representation of the Hotel object.
    def __str__(self):
        return "Hotel[Name:" + self._name + ", Location: " + self._location + ", Rooms:" + str(len(self._rooms)) + "]"


# ServiceRequest Class
class ServiceRequest:
    """ a class that represents a request for additional services by a guest."""

    def __init__(self, request_id, service_type, status="Pending"):
        #initialize service request attributes as private.
        self.__request_id = request_id  #each service request has a unique identifier
        self.__service_type = service_type  # Type of service requested.
        self.__status = status  #the status of the request (default is "Pending").

    #Getter method to get the request ID
    def get_request_id(self):
        return self.__request_id

    #Setter method to update the request ID
    def set_request_id(self, request_id):
        self.__request_id = request_id

    #Getter method to get the type of service requested
    def get_service_type(self):
        return self.__service_type

    #Setter method to update the type of service requested
    def set_service_type(self, service_type):
        self.__service_type = service_type

    #Getter method to get the status of the service request
    def get_status(self):
        return self.__status

    #Setter method to update the status of the service request
    def set_status(self, status):
        self.__status = status

    #Method to return a string representation of the ServiceRequest object.
    def __str__(self):
        return "ServiceRequest[ID: " + str(self.__request_id) + ", Type: " + self.__service_type + ", Status: " + self.__status + "]"
