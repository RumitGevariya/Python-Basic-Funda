#The id is the object's memory address, and will be different for each time you run the program. 
#(except for some object that has a constant unique id, like integers from -5 to 256)
x =['rumit','abhay']
y =['rumit','abhay']
print(id(x))
print(id(y))
print(x is y)
c ='a'
print(id(c))


x=10
y=11
z=x
print(id(z))
print(id(x))
print(id(y))
print(x is y)
