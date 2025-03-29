# Booking Class
class Booking:
    """ a class to represents the booking made by a guest."""

    def __init__(self, booking_id, check_in_date, check_out_date, status="Confirmed"):
        #initialize booking attributes as private
        self.__booking_id = booking_id  #identifier for the booking
        self.__check_in_date = check_in_date  #Check-in date for the booking
        self.__check_out_date = check_out_date  #Check-out date for the booking
        self.__status = status  # Booking status (default is "Confirmed")

    #Getter method to get the booking ID
    def get_booking_id(self):
        return self.__booking_id

    #Setter method to update the booking ID
    def set_booking_id(self, booking_id):
        self.__booking_id = booking_id

    #Getter method to get the check-in date
    def get_check_in_date(self):
        return self.__check_in_date

    #Setter method to update the check-in date
    def set_check_in_date(self, check_in_date):
        self.__check_in_date = check_in_date

    #Getter method to get the check-out date
    def get_check_out_date(self):
        return self.__check_out_date

    #Setter method to update the check-out date
    def set_check_out_date(self, check_out_date):
        self.__check_out_date = check_out_date

    #Getter method to get the booking status
    def get_status(self):
        return self.__status

    #Setter method to update the booking status
    def set_status(self, status):
        self.__status = status

    #Method to return a string representation of the Booking object.
    def __str__(self):
        return "Booking[ID=" + str(self.__booking_id) + ", Check-In=" + str(self.__check_in_date) + ", Check-Out=" + str(self.__check_out_date) + ", Status=" + self.__status + "]"


# Feedback Class
class Feedback:
    """a class that represents the guest feedback for a hotel stay."""

    def __init__(self, rating, comments, timestamp):
        #initialize feedback attributes as private
        self.__rating = rating  #Rating given by the guest (out of 5 stars)
        self.__comments = comments  #Comments provided by the guest
        self.__timestamp = timestamp  #Timestamp when the feedback was given

    #Getter method to get the rating
    def get_rating(self):
        return self.__rating

    #Setter method to update the rating
    def set_rating(self, rating):
        self.__rating = rating

    #Getter method to get the comments.
    def get_comments(self):
        return self.__comments

    #Setter method to update the comments
    def set_comments(self, comments):
        self.__comments = comments

    #Getter method to get the timestamp
    def get_timestamp(self):
        return self.__timestamp

    #Setter method to update the timestamp
    def set_timestamp(self, timestamp):
        self.__timestamp = timestamp

    #method to return a string representation of the Feedback object
    def __str__(self):
        return "Feedback[Rating=" + str(self.__rating) + ", Comments=" + self.__comments + ", Timestamp=" + str(self.__timestamp) + "]"


# Staff Class
class Staff:
    """a class that represents the hotel staff members"""

    def __init__(self, staff_id, name, position):
        #initialize staff attributes as private.
        self.__staff_id = staff_id  # ID for the staff member
        self.__name = name  #Name of the staff member
        self.__position = position  #Job position of the staff member

    #Getter method to get the staff ID.
    def get_staff_id(self):
        return self.__staff_id

    #Setter method to update the staff ID
    def set_staff_id(self, staff_id):
        self.__staff_id = staff_id

    #Getter method to get the staff member's name
    def get_name(self):
        return self.__name

    #Setter method to update the staff member's name
    def set_name(self, name):
        self.__name = name

    # Getter method to get the staff member's position
    def get_position(self):
        return self.__position

    #Setter method to update the staff member's position
    def set_position(self, position):
        self.__position = position

    #Method to return a string representation of the Staff object
    def __str__(self):
        return "Staff[ID=" + str(self.__staff_id) + ", Name=" + self.__name + ", Position=" + self.__position + "]"