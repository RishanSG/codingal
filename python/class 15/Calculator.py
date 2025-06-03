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

while True:
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Power")
    choice=int(input("Enter choice: "))
    num=int(input("Enter a number: "))
    num2=int(input("Enter a number: "))

    if choice==1:
        add(num,num2)
    elif choice==2:
        sub(num,num2)
    elif choice==3:
        multiply(num,num2)
    elif choice==4:
        div(num,num2)
    elif choice==5:
        power(num,num2)