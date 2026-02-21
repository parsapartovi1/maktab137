##1
from datetime import datetime
from email.utils import parseaddr
from itertools import count


# date = a library to get the system time
# hour = datetime.now().hour = returns a number between 0 ... 23 -> " 24 hours "
# print(hour)
#we want to get parameters so we need 3 functions always!!!

def restrict_time(start_time = 6 , end_time = 12):   #main decorator , this function only gets two parameters
                                                     # to decide what time to start and end

    def decorator(func):   #makes the main function (restrict_time) ready to become a decorator

        def wrapper(*args,**kargs): # the one which actually does the job while calling the decorator and those two
                                    # parameters let the function to g*et any input and checks the time condition

            hour = datetime.now().hour # gets the current time from system the 3:20 would be 3
            if start_time <= hour <= end_time:# this one sees if the current time is in the gave time to work or not
                print("working...")
                return func(*args,**kargs)
# print("working...")
# return func(*args,**kargs)
            else:
                print("not working...")
                return None # if function couldn't work (was out of time span ) says function didnt work
                            #so the value od none gets shown instead
        return wrapper # to replace wrapper by the main function
    return decorator
# restrict_time(start_time=6, end_time=12)
@restrict_time(1 , 2)
def work():
    print("working...")
work()