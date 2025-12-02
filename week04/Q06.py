##6

input1 = "aBcD"
input2 = "ABcd"
count = 0
for index in range(len(input1)): # were iterating from index zero till len input one
                                # input 1 or two no metter if they were different we'll choose the smaller one
    if input1[index] != input2[index]:
        count += 1

print(count)