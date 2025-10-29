numbers=[2,3,4,7,8,9,14,18,20,22,32,23,9]

#squarelist=[]

#for n in numbers:
#   square = n**2
#   squarelist.append(square)
#print(squarelist)

squarelist=[x**2 for x in numbers if x<20]
print(squarelist)