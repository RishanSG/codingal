x=int(input("Enter cost price: "))
y=int(input("Enter sale price: "))

z= y-x

if z > 0:
    print("profit has been made")

elif z < 0:
    print("Loss has been made")
elif z==0 :
    print("neither loss nor profit has been made")