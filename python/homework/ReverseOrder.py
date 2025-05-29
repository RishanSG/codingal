x=int(input("Enter number: "))
x1=x
y=0
while x>0:
    digit=x%10
    y+=1
    x=x//10
print(f"There are {y} digits in the number {x1}")