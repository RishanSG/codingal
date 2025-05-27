number=int(input("Enter a number: "))
number1=number
x=len(str(number))
y=0
z=0
while number>0:
    digit=number%10
    y=digit**x
    z+=y
    number=number//10
if z==number1:
    print(f"Number {number1} is an armstrong number")
    





