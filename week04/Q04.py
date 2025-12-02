##4
"""
why a periodic function ?
well ; we want to continue calculating until we reach the elements cause our list has sublist and each element
could be inside another list so we are using it to get within the layers .
"""
def nested_sum(lst):
    total = 0  # to keep the final sum and element by element gets increased 1 + After period(A.P) --> +2 -> +3
                # A.P -> +4 -> A.P -> +5 == 15
    for item in lst:
        if isinstance(item, list): # isinstance to check if item is list or not (two arguments ) and then down below
                                    #things

            total += nested_sum(item)  # we are using periodic function just in case some our
                                        #elements are within another list(sublist) so whenever while calculating
                                        # we end up to sub ones we get the inner elements to sum
        else:
            total += item # if it was in the main list(not in sub list) it directlly goes for calculating
                            #if not goes for periodic func to calculate inner element
    return total

print(nested_sum([1, [2, 3], [4, [5]]]))