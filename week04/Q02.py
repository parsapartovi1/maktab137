# @restrict_time(start =0 , end = 24)
# def work() :
#     print("working...")
# work()


##2

def string_maker(func):  # the first decorator , funk is the function which gonna
                        #become decorator(gets the main function and changes its behavior
    def wrapper(*args, **kwargs):  # the inner function is th one which is doing the job and args because we
                                # we are getting anything as function input so it should be a tuple of things
                                # ( checks the inputs )
        new_args = []  # an empty list to append the str converted ones in it . (line "append()")
        for arg in args:  # to iterate all the function input( arguments )
            make_string = str(arg)  # converting job
            new_args.append(make_string)  # after converting we're now appending it into our empty list
        return func(*new_args, **kwargs)  # to ejra our function because it has done the thing we wanted and now its
                                        # output turn !
    return wrapper  # to replace our actuall working function with the main one


def len_something(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            print(f"the len of '{arg}' is {len(arg)}")  # our previous decorator has done the str job already
        return func(*args, **kwargs)

    return wrapper


# here we are making our two decorators into one function :
@len_something
@string_maker
def both_function(any):
    print(f"string converted --> {user_input} is now str type")

user_input = input("Enter something: ")
both_function(user_input)