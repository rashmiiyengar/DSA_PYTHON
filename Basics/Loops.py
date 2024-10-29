list=[1,2,3,4,5,6,7,8]

count=1
while count<=5:
    print("hello",count)
    count+=1

count1=3
while count1>0:
    print(count1)
    count1=count1-1
    
#print numbers from 1 to 50

count2=1
while count2 <=5:
    print(count2)
    count2+=1

#print the multiplication table of n
multiplicationTable=int(input("Enter the multiplication table: "))

multiply=1
while multiply<=10:
    print(f"{multiplicationTable} * {multiply} ={multiplicationTable * multiply}")
    multiply+=1

#print the elements of the following list using a loop
list1=[1,4,5,6,7,2,9,10,11,19]
idx=0
while idx <= len(list1)-1:
    print(list1[idx])
    idx+=1

#Search for a number x in this tuple using loop
tuple1=(2,4,6,8,10,12,14)
x= int(input("enter the number from tuple: "))
idx1=0

while idx1 <=len(tuple1)-1:
    if(tuple1[idx1] == x):
        print(tuple1[idx1])
        print(tuple1.index(2))
    idx1+=1