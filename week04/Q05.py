##5


def File_io(input_file="input.txt", output_file="output.txt"): # makes decorator
    def decorator(func): # main decorator (gets the main function and changes it )
        def wrapper(data): # wrapper = process_data (the one who adds the behavior )
            with open(input_file, "w", encoding="utf-8") as f:
                f.write(str(data))

            result = func(data) # running the main function with data and putting into result
                                # data is the input we gave to proccess data
                                # func = the main function that decorator goes on

            with open(output_file, "w", encoding="utf-8") as f_out:
                f_out.write(str(result))  # in str(result) we make sure data is str (like if it was num

            return result
        return wrapper
    return decorator


@File_io(input_file="input.txt", output_file="output.txt")
def process_data(data):
    return data.upper()

process_data("parsa here")  # the output would be PARSA HERE