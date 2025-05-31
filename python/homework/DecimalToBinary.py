num=int(input("Enter Decimal Number: "))
x=''
while num>0:
    digit=num%2
    digit=str(digit)
    x=x+digit
    num=num//2

print(x[::-1])

