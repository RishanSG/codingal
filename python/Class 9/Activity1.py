x=input("Did you have a medical condition? (Y for yes and N for No): ").upper()
if x=="Y" :
    print("Allowed to write the exam")
elif x=="N" :
    y=input("Is attendance above 75?(Y for yes and N for no): ").upper()
    if y=="Y":
        print('Allowed to write the exam')
    elif y=='N':
        print("Not allowed to write the exam")