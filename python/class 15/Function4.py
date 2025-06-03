def add(a,b):
    print(f"{a}+{b}={a+b}")
def sub(a,b):
    print(f"{a}-{b}={a-b}")
def multiply(a,b):
    print(f"{a} x {b}={a*b}")
def div(a,b):
    print(f"{a}/{b}={a/b}")
def power(a,b):
    print(f"{a} raised to the power {b} = {a**b}")
num=int(input("Enter a number: "))
num2=int(input("Enter a number: "))

add(num,num2)
sub(num,num2)
multiply(num,num2)
div(num,num2)
power(num,num2)