#HOME WORK 2 :

quiz:int = int(input("Enter a number(xxxx): "))
x1 = int(quiz // 2 -1)
x2 = int(x1 // 2+1)
x3 = int(x2 //2 +1 )

print((x1 , x2 , x3) ,  quiz)
if x1 + x2 + x3 == quiz  :
    print("YES")
else :
    print("NO")