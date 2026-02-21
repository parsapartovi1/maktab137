#HOME WORK 4 :

name = input("Enter your name: " )
score = int(input("Enter your score: "))
if score >= 90 :
    print(f"{name}: Perfect ")
elif 70 < score < 90 :
    print(f"{name}: Good ")
elif score <= 70 :
    print(f"{name}: need improvement ")
else :
    print("enter the valid information")