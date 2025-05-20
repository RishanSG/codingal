#print(ord('a'))
#print(ord('z'))
#print(ord('A'))
#print(ord('Z'))

x=((input("Enter character to see if it is an alphabrt or not: ")))
y=ord(x)

if 65<=y<=90 or 97<=y<=122:
    print(f"the character {x} is an alphabet")
else:
    print(f"the character {x} is not an alphabet")