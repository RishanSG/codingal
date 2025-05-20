x=10
y=10
print(id(x))
print(id(y))

print(x is y)
print(x is not y)


y=11

print(x is y)
print(x is not y)

a=[2,3,4]
b=[2,3,4]

print(a is b)
print(id(a))
print(id(b))

a=[2,3,4]
name="sakash"
print(20 in a)
print