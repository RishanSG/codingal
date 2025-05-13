M=float(input("Maths marks: "))
S=float(input("Science marks: "))
E=float(input("English Marks: "))
F=float(input("French marks: "))
SS=float(input("Social Studies: "))
T= SS+F+E+S+M
O=100*5

Percentage=T/O*100

if 90<=Percentage<=100:
    print("Grade A")
elif 75<=Percentage<=89:
    print("Grade B")
elif 50<=Percentage<=74:
    print("Grade C")
elif 0<=Percentage<=49:
    print("Grade D")