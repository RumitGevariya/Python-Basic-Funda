#set :unoreded,unidexing,

s1 ={1,3,4,5,6,4}
s2 ={1,2,3,2,2,3,2}
'''
#print(s1)
#print(s2)
s1.add(0)
#print(s1)
s1.update((9,8))
#print(s1)
s2.update([9,0])
s2.remove(1)
print(s2)
#for i in s1:
    #print(i)'''
print(s1|s2)
print(s1&s2)
print(s1-s2)
print(s2-s1)

#set to list
s ={1,2,3,2,3,5}
print(type(s))
c =list(s)
print(c)

