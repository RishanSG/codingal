list1 = [1,2,3,4,5,1,2,3]
set1={1,2,3,4,5,1,2,3}
print(list1[0])
#set does not have an index unlike lists
print(set1)

#Set does not print duplicate numbers unlike lists
print(set1)
print(list1)
#union and intersection and difference and symmetrical difference
setA={1,2,3,4}
setB={2,4,5,6}
print("setA", setA)
print("setB", setB)
#union
print("Set A union set B", setA.union(setB))
    #we can also use '|'
print("Set A union set B", setA | setB)


print("set A intersection set B", setA.intersection(setB))
    #we can also use '&'
print("setA intersection set B", setA & setB)

#difference

print("set a- set b", setA.difference(setB))
    #we can also use '-'
print("set A - set B", setA - setB)

print("set A symmetrical difference set B",setA.symmetric_difference(setB))
    # we can also use '^'
print("set A symmetrical difference set B", setA ^ setB)

#add function which adds an element to the set
setA.add(100)
print(setA)