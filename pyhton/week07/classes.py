class User:
    def __init__(self, name: str , family_name: str,
                 user_name: any ,birthday: str,number: str , password: str
                 ,user_id, signup_time):


        self.name = name
        self.family_name = family_name
        self.birthday = birthday
        self.user_name = user_name
        self.number = number
        self.password = password
        self.user_Id = user_id
        self.signup_time = signup_time
        # self.login_info = login_info if login_info is not None else []



class Travel:
    def __init__(self, origin, destination, travel_date,
                 travel_duration, total_capacity, available_capacity,
                 price, user_id, travel_id):
        self.origin = origin
        self.destination = destination
        self.travel_date = travel_date
        self.travel_duration = travel_duration
        self.total_capacity = total_capacity
        self.available_capacity = available_capacity
        self.price = price
        self.user_id = user_id
        self.travel_id = travel_id





class Ticket :
    def __init__(self, user_id, travel_id
                 , seat_number , status,ticket_id ,timestamp ) :

        self.user_id = user_id
        self.travel_id = travel_id
        self.seat_number = seat_number
        self.status = status
        self.ticket_id = ticket_id
        self.timestamp = timestamp


class Payment :
    def __init__(self , user_id , travel_id , amount, timestamp , status , payment_id):
        self.user_id = user_id
        self.travel_id = travel_id
        self.amount = amount
        self.timestamp = timestamp
        self.status = status
        self.payment_id = payment_id
