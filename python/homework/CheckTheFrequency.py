testdictionary={
    "Codingal" : 3 ,
    "platform" : 3 ,
    "is"  : 2 ,
    "the" : 2 ,
    "best" : 2 ,
    "for" : 1 ,
    "coding" : 1 ,

}
user_input=int(input("Enter value: "))
freq=(list(testdictionary.values()).count(user_input))
print("The frequency of", user_input, "is", freq)