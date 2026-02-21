##3

def most_frequent(input_list):
    if not input_list:
        return None    #because we don't want to get any errors and our function stop itself (list should not be empty
                        # we want to work with it

    frequency = {}   # a dictionary to keep each element as a key save the frequency as a value and to count the
                    # frequency of each element
    for item in input_list:
        if item in frequency:
            frequency[item] += 1# if the item was already there and again is there we plus one to it .
        else:
            frequency[item] = 1 # if it's the first time that an item is in our dict we consider it as one(first time)
            # print(frequency[item])

    max_count = 0
    most_common = None
    for key in frequency:
        if frequency[key] > max_count:  # checks if the considered item (key) id more than max or not ! ( 0 )
            max_count = frequency[key] # if it was we update the value of max to that
            most_common = key # the actuall element  we want to get in return
                                # we are saving the most frequent in a variable

    return most_common


user_input = input("Enter the elements: ")
user_input = user_input.replace(" ", ",") # if this line didn't exicted our whole input would be one
                                                        # like ['2 3 2 5 2']
input_list = user_input.split(",") # to transform our str inputs into list , here we separate each input
                                    # with comma (,) our function wants to count frequency so we need a list
print(f"The most frequent item is: {most_frequent(input_list)}")