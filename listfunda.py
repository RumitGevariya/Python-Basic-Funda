#data stracture
#1)list :"changeble","indexing","ordering"
list method
1)append
2)len
3)insert
4)pop
5)del
6)clear

#example list
list =['hello','rumit','how','are','you','done']
for i in list:
    print(i[0])
    
#iterate list value using while loop:
list =['hello','rumit','how','are','you','','done']
i =0
while len(list)>i:
    if list[i]=='':
        i =i+1
        continue
    print(list[i][0])    
    i =i+1
    
#example
list =['hello','rumit','how','are','you','done']
for i in enumerate(list):
    print(i)
    print(i[1][0])
    
#example
a =['a','b','c','d','e',1,2,3]
#using replace function
a[3:5] =[2,4]
print(type(a))
print(a)
#delet values
del(a[3:5])
print(a)


#example
a =[['a','b','v'],[1,2,3],['z',[9],'hello']]
b =a[2][1][0]
print(b)


#3) list to other
a =['1','2','v',3]
print(type(a))
print(type(tuple(a)))
s =set(a)
print(s)
c =str(a)
print(c)
print(a)


#example list3)
list =['a','d','s',None,'a']
for i in list:
    if i==None:
        continue
    print(i[0])
    
    
#example list2)
list =['vishal','rumit','jay','','Manish']
for i in list:
    if i =='':
        continue
    print(i[0])    
    
    
    
    
    
