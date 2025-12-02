## 7
def suming(input1  , input2 , /):
    x = input1 + input2
    print(x)
suming(2 , 32)

##7
def printing(*, age = 2 , name = "p" ):
    print(f"{age} ,\n {name}")
printing(age = 2 ,name =" parsa")


##7
def calculator(num1 , num2 , / ,* , calcu):
    # calcu = input("enter the operator(* , / , + , -) : ")
    if calcu == "*":
        product = num1 * num2
        print(f"{num1} * {num2} = {product}")
    if calcu == "/":
        division = num1 / num2
        print(f"{num1} / {num2} = {division}")
    if calcu == "+":
        addition = num1 + num2
        print(f"{num1} + {num2} = {addition}")
    if calcu == "-":
        subtraction = num1 - num2
        print(f"{num1} - {num2} = {subtraction}")

calculator(5 , 10 , calcu = "*")