x=int(input("enter your amount: "))
x1=x//1000
a=x*x1
x2=a%1000

y=x2//500
b=x2*y
y2=b%500

z=y2//100
c=y2*z
z2=c%100

print(f"There are {x1} 1000 rupee notes, {y} 500 rupee notes, and {z} 100 rupee notes and the reamining money is {z2}")