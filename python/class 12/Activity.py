num=int(input("Enter a number: "))
sumOfDigits=0
odd=0
even=0
while num > 0:
    digit = num % 10
    sumOfDigits += digit
    num=num//10
    if digit%2!=0:
        odd+=1
    elif digit%2==0:
        even+=1


print(f"There are {odd} odd digits and {even} even digits in this number")

print(f"Sum of digits {sumOfDigits}")