try:
    age=int(input("Enter age: "))
    if  age%2==0:
        print(f"Your age, {age}, is an even number")
    elif age%2!=0:
        print(f"Your age, {age}, is an odd number")
except ValueError:
    print("You must enter a number (no decimals!)!")
except Exception as e:
    print("Something went wrong!")

