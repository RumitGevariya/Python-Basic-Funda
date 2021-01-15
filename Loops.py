#while loop:
i =1
a =int(input("how many student: "))
while i<=a:
    name =input("enter name :")
    i =i+1
print("done")    


#for loop
a =int(input("enter how many stu: "))
for i in range(a):
    name =input("enter a name: ")
    subj =int(input("enter subj: "))
    total =0
    for j in range(subj):
        marks =int(input("enter a marks"))
        total =marks+total
    print(total)
print("recoded")   



#example 2
a =int(input("enter how many stu: "))
i =0
while a>i:
    name =input("enter a name: ")
    subj =int(input("enter a subj: "))
    j =0
    total =0
    while subj>j:
        mark =int(input("enter a mark: "))
        total =total+mark
        j =j+1
    print(total)  
    i =i+1
print("recoded")  
