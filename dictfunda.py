2)Dictionary:unordered,indexing,changebale
    mutable.....
methods::
1)zip

d ={'a':200,'b':20,'c':12}
y =enumerate(d)
print(tuple(y))


#accessing value
d ={'a':200,'b':20,'c':12}
l1 =[]
a =['a','b','c']
m =[20,68,76]
d =dict(zip(a,m))
print(d)
l1 =[]
l2 =[]
for i in d.keys():
    print(i)
    
for i in d.values():
    print(i)

for i,j in d.items():
    a =i
    b =j
    l1.append(a)
    l2.append(b)
print(l1)
print(l2)
#add to list
print(l1+l2)
#using zip function
c =zip(l1,l2)
l2 =[]
#print(d['a'])
for i in d.keys():
    print(i)
print("\n")
for i in d.values():
    print(i)
print("\n")
for i,j in d.items():
    l1.append(i)
    l2.append(j)    
c =dict(zip(l1,l2))
print(c)
print("\n")
#change values
c['a'] =400
print(c)
#find length
len(c)
#add item



#above example with batter way
a =int(input("how many student have!!.."))
Stu_Name =[]
Mark_Total=[]
Per =[]
Grade =[]
l2 =[]
l3 =[]
l4 =[]
for i in range(a):
    name =input("enter a name of the student!..")
    Stu_Name.append(name)
    subj =5
    j=1
    total =0
    while subj>=j:
        marks =int(input("please enter a marks of five subj out of 100!..."))
        total =total+marks
        j =j+1
    Mark_Total.append(total)    
    c =str(((total*100)/500))+"%"
    Per.append(c)
print("recoded")        
l1 =dict(zip(Stu_Name,Per))
print(l1)



#convert dict to other
d ={1:'rumit',2:'jay',3:'manish',4:'krunal'}
e =str(d)
print(e)
print(len(e))
print("\n")
z =list(e)
print(z)
print(len(z))
print("\n")
t =str(z)
print(t)
print(len(t))
print(set(d))


