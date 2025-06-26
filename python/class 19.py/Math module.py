import math
def add (a,b):
    return a + b
def sin(x):
    return math.sin(math.radians(x))

while True:
    print("1. Add the two numbers")
    print("2. Trigonometrical Functions")
    print("3.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        num1=float(input("Enter 1st number:"))
        num2=float(input("Enter 2nd number:"))
        print("The sum is ", add(num1,num2))
    elif choice==2:
        print("1.sin")
        print("2.cos")
        print("3.tan")
        choice=int(input("Enter your choice: "))
        if choice==1:
            x = float(input("Enter the angle in degrees: "))
            print("the sine of",x,"is",sin(x))
        elif choice==2:
            x= float(input("Enter angle in degrees: "))
            print("the cos of", x, "is",math.cos(math.radians(x)))
        elif choice==3:
            x= float(input("Enter the angle in degrees: "))
            print("The tangent of",x, "is", math.tan(math.radians(x)))
                  
