import pickle
import os
import re
import uuid
import hashlib
import random
from datetime import datetime
from classes import User

current_user = None

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def sign_up():
    while True:
        names = input("Enter your name: ")
        if  names and re.search(r"[@#$%^&*()_+= 0-9]", names):
            print("Enter a valid name")
            continue
        break

    while True:
        family_name = input("Enter your family name: ")
        if  family_name and re.search(r"[@#$%^&*()_+= 0-9]", family_name):
            print("Enter a valid family name")
            continue
        break

    while True:
        birth_date = input("What's your birth date (yyyy/mm/dd): ")
        if "/" in birth_date:
            parts = birth_date.split("/")
            if len(parts) == 3 and all(part.isdigit() for part in parts):
                break
        print("Enter a valid date")

    while True:
        user_name = input("Choose a username: ")
        if not user_name or re.search(r"[#%^&*!/]", user_name):
            print("Enter a valid username (no symbols)")
            continue
        break

    while True:
        number = input("Enter your phone number: ")
        if not number.isdigit() or len(number) != 11:
            print("Enter a valid 11-digit number")
            continue
        break

    while True:
        password = input("Choose a password: ")
        if len(password) < 8:
            print("Password must be at least 8 characters long")
            continue
        again2 = input("Please reenter your password: ")
        if password != again2:
            print("Passwords do not match")
            continue
        break

    hashed_password = hash_password(password)
    user_id = str(uuid.uuid4())
    signup_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    user = User(names, family_name, user_name, birth_date, number, hashed_password, user_id, signup_time)

    file_name = "users"

    if os.path.exists(file_name):
        with open(file_name, "rb") as f:
            try:
                user_data = pickle.load(f)
            except EOFError:
                user_data = {}
    else:
        user_data = {}

    if number in user_data:
        print("You have already signed up")

    else:
        user_data[number] = user
        with open(file_name, "wb") as f:
            pickle.dump(user_data, f)
        print("Sign up successful!")
        print("Your ID:", user_id)
        print("Signed up at:", signup_time)

sign_up()


def login():
    file_name = "users"

    if not os.path.exists(file_name):
        print("No users have signed up yet.")


    with open(file_name, "rb") as f:
        try:
            user_data = pickle.load(f)
        except EOFError:
            print("User data file is empty.")
            return

        number = input("Enter your phone number: ")
        password = input("Enter your password: ")
        hashed_input = hash_password(password)

        if number not in user_data:
            print("This number is not registered. Please sign up first.")
            return

        user = user_data[number]
        if user.password != hashed_input:
            print("Incorrect password. Try again.")
            return

        print("Welcome back,", user.name, user.family_name)
        print("Your ID:", user.user_Id)
        print("Signed up at:", user.signup_time)
    global current_user
    current_user = user

login()

from classes import Travel
def search_travel():

    global current_user
    if current_user is None:
        print("You must be logged in to search for travel.")
        return

    travel_list = [
        "tehran", "gilan", "alborz", "ardabil", "bushehr", "chaharmahal bakhtiari",
        "east azerbaijan", "west azerbaijan", "fars", "golestan", "hamadan", "hormozgan",
        "ilam", "isfahan", "kerman", "kermanshah", "boyer-ahmad", "kurdistan",
        "lorestan", "markazi", "mazandaran","qazvin", "qom", "mashhad",
        "semnan", "sistan", "khorasan", "khuzestan", "yazd", "zanjan"]
    while True :
        origin = input("Choose your origin: ")
        if origin not in travel_list:
            print("Enter a valid origin")
            continue
        break

    while True :
        destination = input("enter your destination: ")
        if destination not in travel_list:
            print("Enter a valid destination: ")
            continue
        break

    while True :
        print("enter your travel date".center(50, "."))
        current = input("do you want to travel today (yes/no)? :")
        if current == "yes" :
            travel_time =  datetime.now().strftime("%Y/%m/%d at %H:%M:%S")
            print("your travel time is", travel_time)
            break
        if current != "yes" :
            day = input("enter the day you want to travel:(0x) ")
            month = input("enter the month you want to travel(0x): ")
            year = input("enter the year you want to travel(xxxx): ")
            clock_h = input("at what hour?(xx): ")
            clock_m = input("at what minute?(xx): ")
            if not (day.isdigit() and month.isdigit() and year.isdigit()):
                print("Enter a valid date")
                continue
            if not clock_h.isdigit():
                print("Enter a valid hour")
            if not clock_m.isdigit():
                print("Enter a valid minute")
                continue
            travel_time = f"{clock_h.zfill(2)}:{clock_m.zfill(2)}"
            if day.isdigit() and month.isdigit() and year.isdigit():
                print(f"your travel date is:{year}/{month}/{day} at {travel_time} o'clock")
        else:
            print("Please answer with 'yes' or 'no'")
        continue



    travel_options = [
        {"route": "Tehran to Shiraz", "price": 450_000, "time": "08:30"},
        {"route": "Mashhad to Isfahan", "price": 380_000, "time": "14:15"},
        {"route": "Tabriz to Kish", "price": 620_000, "time": "06:45"},
        {"route": "Yazd to Rasht", "price": 500_000, "time": "12:00"},
        {"route": "Qom to Ahvaz", "price": 410_000, "time": "09:20"},
        {"route" : "tehran to gilan" , "price" : 250000 ,"time" : "10:30" },
    ]

    # selected_travels = random.sample(travel_options, 4)

    with open("available_travels.txt", "w") as file:
        for travel in travel_options:
            line = f"\n{travel['route']},{travel['price']},{travel['time']}\n"
            file.write(line)

    with open("available_travels.txt", "w") as file:
        for travel in travel_options:
            line = f"\n{travel['route']},{travel['price']},{travel['time']}\n"
            file.write(line)

    # def sort_by_price_and_time(travel1):
    #     return travel1["price"],travel1["time"]
    #
    #
    # sorted_travels = sorted(travels, key=sort_by_price_and_time)

    print("All Travel Options:".center(50, "_"))
    for travel in travel_options:
        print(f"{travel['route']} | {travel['price']} Toman | travel time: {travel['time']}")


    print("your travel options:".center(50, "_"))
    matched_route = f"{origin} to {destination}"
    for option in travel_options:
        if option["route"].lower() == matched_route:
            matched_travel = option
            print(matched_travel)
            break

    user_travel = Travel(
        origin=origin, destination=destination , travel_date = travel_time, travel_duration=120 ,
        total_capacity=40 ,available_capacity=20 ,price=matched_travel["price"] , user_id=current_user.user_Id ,
        travel_id=str(uuid.uuid4()) )

    travel_file = "travels"
    if os.path.exists(travel_file):
        with open(travel_file, "rb") as f:
            try:
                travel_data = pickle.load(f)
            except EOFError:
                travel_data = []
    else:
        travel_data = []

    travel_data.append(user_travel)

    with open(travel_file, "wb") as f:
        pickle.dump(travel_data,f)
    print("now check again to reserve: " . center(50, "*"))

    # with open(travel_file, "rb") as f:
    #     print(pickle.load(f))


search_travel()




from classes import Ticket

def reservation():
    global current_user
    if current_user is None:
        print("You must be logged in first for reservation.")
        return

    travel_file = "travels"
    if not os.path.exists(travel_file):
        print("we're sorry ; No travel route founded.")
        return

    with open(travel_file, "rb") as f:
        try:
            travel_data = pickle.load(f)
        except EOFError:
            print("no existing travel yet .")
            return

    origin = input("Enter your origin to check: ").strip().lower()
    destination = input("Enter your destination to check: ").strip().lower()
    matched_route = f"{origin} to {destination}"

    matched_travel = None
    for t in travel_data:
        route = f"{t.origin.lower()} to {t.destination.lower()}"
        if route == matched_route:
            matched_travel = t
            break

    if not matched_travel:
        print("No matching travel found for this route.")
        return

    print(f"Travel founded: {matched_travel.origin} to {matched_travel.destination}"
          f" on {matched_travel.travel_time}")


    available_seats = list(range(1, matched_travel.total_capacity + 1))
    reserved_seats = []

    seat = input("Choose your seat number: ").strip()
    if not seat.isdigit():
        print("Invalid seat input.")
        return

    seat = int(seat)
    if seat not in available_seats:
        print("Seat not available.")
        return

    if seat in reserved_seats:
        print("Seat is taken .")
        return

    ticket = Ticket(
        user_id=current_user.user_Id,
        travel_id=matched_travel.travel_time,
        seat_number = seat,
        status="reserved",
        ticket_id=str(uuid.uuid4()),
        timestamp=datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

    ticket_file = "tickets"
    if os.path.exists(ticket_file):
        with open(ticket_file, "rb") as f:
            try:
                ticket_data = pickle.load(f)
            except EOFError:
                ticket_data = []
    else:
        ticket_data = []

    ticket_data.append(ticket)

    with open(ticket_file, "wb") as f:
        pickle.dump(ticket_data, f)

    reserved_seats.append(seat)

    print("Your ticket has been reserved successfully!".center(50, "~"))
    print("~".center(49, "~"))
    print(f"Ticket ID: {ticket.ticket_id} | Seat: {seat} | Status: {ticket.status}")
    print(f" reserved date and time : {ticket.timestamp}")
    busses = ["scania" , "bogie" , "maral" , "volvo"]
    random_choice = random.choice(busses)
    print(f"bus name : {random_choice}")
    print("~".center(49, "~"))
    print("~".center(49, "~"))
reservation()







from classes import Payment
def payment():
    global current_user
    if current_user is None:
        print("You must be logged in to make a reservation.")
        return

    ticket_file = "tickets"
    travel_file = "travels"
    payment_file = "payments"

    #tickets
    if not os.path.exists(ticket_file):
        print("No travel data found.")
        return

    with open(ticket_file, "rb") as f:
        try:
            ticket_data = pickle.load(f)
        except EOFError:
            print("You have no reservation yet.")
            return

    # travels
    if not os.path.exists(travel_file):
        print("Travel data missing.")
        return

    with open(travel_file, "rb") as f:
        try:
            travel_data = pickle.load(f)
        except EOFError:
            print("No travel info available.")
            return

    print("Payment Section".center(50, "_"))
    print("Thank you for your honest choice".center(50, "-"))

    while True:
        ticket_code = input("Enter your Ticket ID: ").strip()
        if re.search(r"[@#$%^&*()_+=]", ticket_code):
            print("Enter your Ticket ID correctly.")
            continue

        matched_ticket = None
        for t in ticket_data:
            if t.ticket_id == ticket_code:
                matched_ticket = t
                break

        if not matched_ticket:
            print("Ticket ID not found.")
            continue

        if matched_ticket.status == "paid":
            print("This ticket has already been paid.")
            return

        break

    matched_travel = None
    for tr in travel_data:
        if tr.travel_time == matched_ticket.travel_id:
            matched_travel = tr
            break

    if not matched_travel:
        print("Travel info not found.")
        return

    price = matched_travel.price
    print(f"Your debt is: {price} Toman")

    # Payment
    while True:
        pay = input("Enter the amount to pay: ").strip()
        if not pay.isdigit():
            print("Invalid amount.")
            continue

        pay = int(pay)
        if pay < price:
            print("Your paying amount is less than your price!")
            continue


        if pay > price:
            refund = pay - price
            print(f"Your refund: {refund} Toman")

        print("Your debt got paid successfully!")

        # Update status
        matched_ticket.status = "paid"

        # Save updated ticket data
        with open(ticket_file, "wb") as f:
            pickle.dump(ticket_data, f)

        # Creating payment file
        payment = Payment(
            user_id = current_user.user_Id,
            travel_id = matched_ticket.travel_id,
            amount = pay,
            timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
            status="successful",
            payment_id=str(uuid.uuid4()))

        if os.path.exists(payment_file):
            with open(payment_file, "rb") as f:
                try:
                    payment_data = pickle.load(f)
                except EOFError:
                    payment_data = []
        else:
            payment_data = []

        payment_data.append(payment)

        with open(payment_file, "wb") as f:
            pickle.dump(payment_data, f)

        print("Payment recorded successfully!".center(50, "~"))
        print(f"Payment ID: {payment.payment_id} | Status: {payment.status}")
        print(f"Paid at: {payment.timestamp}")
        break

payment()



def admin():
    while True:
        x = input("Run as administrator? (y/n): ").strip().lower()
        if x == "y":
            try:
                a = int(input("Enter the administrator password: "))
            except ValueError:
                print("Password must be numeric.")
                continue

            if a == 12125050:
                print("Hello admin\n")
                files = ["payment.pkl", "ticket.pkl", "travel.pkl", "users.pkl"]
                for file in files:
                    if os.path.exists(file):
                        print(f"\n--- Contents of {file} ---")
                        try:
                            with open(file, "rb") as f:
                                data = pickle.load(f)
                                print(data)
                        except Exception as e:
                            print(f"Error reading {file}: {e}")
                    else:
                        print(f"{file} not found.")
                break
            else:
                print("Incorrect password.")
        elif x == "n":
            print("Exiting admin mode.")
            break
        else:
            print("Please enter 'y' or 'n'.")
admin()