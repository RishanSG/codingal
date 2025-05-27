number=int(input("enter number : "))
number1=number
x=0
z=0
while number>0:
 number2=number/10
 number=number//10
 y=(number2-number)*10
 x=x+1
 z=z+y
 
z=int(z)
print(f"{number1} has {x} digits")
print(f"sum of digits in the number {number1} is {z}")