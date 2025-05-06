x=int(input("Enter a Number: "))
y=int(input("Enter another Number: "))

print(f"the value of x is {x}")
print(f"type of x is {type(x)}")
print(f"addition of x and y is {x+y}")


# a character string cannot be converted to an integer

x2=False 
y2=int(x2)
print(f"y2 value is {y2}")

x3=-12
y3=bool(x3)
print(f"y3 value is {y3}")

#indexing
x4= "Rishan Sandeep Gadhia"
print(x4[3])

print(x4[7:])
print(x4[7:15])
print(x4[::-1])
