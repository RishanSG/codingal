x=int(input("Enter year: "))
if x%100==0:
     if x%400==0:
        print("Year is leap year")
     else:
        print("Not a leap year")
elif x%4==0:
    print("Leap Year")
else:
    print("Not a Leap Year")


    