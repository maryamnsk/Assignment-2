# Room Class
class Room:
    """a class that represents the hotel room, with details like the type of the room, price, and availability."""

    def __init__(self, room_number, room_type, price_per_night, availability_status=True, amenities=None):
        # Initialize room attributes as private
        self.__room_number = room_number  # each room has a unique room number
        self.__room_type = room_type  # type of room (single, double, suite)
        self.__price_per_night = price_per_night  # cost per night for the room
        self.__availability_status = availability_status  # availability status (True if available, False if not)

        # If amenities is not provided, set it as an empty list
        self.__amenities = amenities if amenities is not None else []

    # Getter method to get the room number
    def get_room_number(self):
        return self.__room_number

    # Setter method to update the room number
    def set_room_number(self, room_number):
        self.__room_number = room_number

    # Getter method to get the room type
    def get_room_type(self):
        return self.__room_type

    # Setter method to update the room type
    def set_room_type(self, room_type):
        self.__room_type = room_type

    # Getter method to get the price per night
    def get_price_per_night(self):
        return self.__price_per_night

    # Setter method to update the price per night
    def set_price_per_night(self, price):
        self.__price_per_night = price

    # Getter method to get the availability status
    def get_availability_status(self):
        return self.__availability_status

    # Setter method to update the availability status
    def set_availability_status(self, status):
        self.__availability_status = status

    # Getter method to get the list of amenities
    def get_amenities(self):
        return self.__amenities

    # Setter method to update the list of amenities
    def set_amenities(self, amenities):
        self.__amenities = amenities

    # Method to return a string representation of the Room object
    def __str__(self):
        return "Room[Number=" + str(self.__room_number) + ", Type=" + self.__room_type + ", Price=" + str(
            self.__price_per_night) + ", Availability=" + str(self.__availability_status) + ", Amenities=" + str(
            self.__amenities) + "]"
    def __repr__(self):
        return self.__str__()  # Ensures it prints properly in lists


# Invoice Class
class Invoice:
    """ a class that represents the invoice for each booking."""

    def __init__(self, total_amount, discounts=0, payment_status="Pending"):
        #initialize invoice attributes as private
        self.__total_amount = total_amount  #Total amount due on the invoice
        self.__discounts = discounts  #Discounts applied to the total amount
        self.__payment_status = payment_status  #Payment status (default is "Pending")

    #Getter method to get the total amount
    def get_total_amount(self):
        return self.__total_amount

    #Setter method to update the total amount
    def set_total_amount(self, total_amount):
        self.__total_amount = total_amount

    #Getter method to get the discount amount
    def get_discounts(self):
        return self.__discounts

    #Setter method to update the discount amount
    def set_discounts(self, discounts):
        self.__discounts = discounts

    #Getter method to get the payment status
    def get_payment_status(self):
        return self.__payment_status

    #Setter method to update the payment status
    def set_payment_status(self, payment_status):
        self.__payment_status = payment_status

    #Method to return a string representation of the Invoice object.
    def __str__(self):
        return "Invoice[Amount=" + str(self.__total_amount) + ", Discounts=" + str(self.__discounts) + ", Status=" + self.__payment_status + "]"


# Payment Class
class Payment:
    """ a class that represents the payment for each invoice"""

    def __init__(self, payment_id, amount, method):
        #initialize payment attributes as private
        self.__payment_id = payment_id  #Unique ID for the payment
        self.__amount = amount  #Amount paid
        self.__method = method  #Payment method (credit card, debit card, mobile wallet).

    #Getter method to get the payment ID
    def get_payment_id(self):
        return self.__payment_id

    #Setter method to update the payment ID
    def set_payment_id(self, payment_id):
        self.__payment_id = payment_id

    #Getter method to get the amount paid
    def get_amount(self):
        return self.__amount

    #Setter method to update the amount paid
    def set_amount(self, amount):
        self.__amount = amount

    #Getter method to get the payment method
    def get_method(self):
        return self.__method

    #Setter method to update the payment method
    def set_method(self, method):
        self.__method = method

    #Method to return a string representation of the Payment object.
    def __str__(self):
        return "Payment[ID=" + str(self.__payment_id) + ", Amount=" + str(self.__amount) + ", Method=" + self.__method + "]"