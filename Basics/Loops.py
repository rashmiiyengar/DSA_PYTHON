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
    
#Break used to terminate the loop when encountyered
#Continue terminates execution in the current iteration and continues execution
#of the loop with the next iteration


count=1
while count<=5:
    if(count==3):
        count+=1
        continue
    print("hello",count)
    count+=1

#For loops are used for sequential traversal for trversing list,strings,tuples

list=[1,2,3,4,5,6,7,8]
tup=(2,4,6,8) #tuples
for el in list:
    print(el)

for element in list: #optional if we want to do something when loop ends
    print(element)
else:
    print("end")
for t in tup:
    print(t)
    
#Range functions returns a sequence of numbers, 
# starting from 0 by default and increments by
#1 (by default) and stops before a specifies number
# range(start?,stop,step?)

for el in range(len(list)):
    print("range elements",list[el])

for el in range(2,len(list)):
    print("range elements with start stop",list[el])

for el in range(2,len(list),2):
    print("step elements",list[el])
    
#pass is a null statement that does nothing 
#it is used as a placeholder for future code.

for el in list:
    pass
print("ele passed succesful")


#WAP to find the sum of first n natural  numbers using while

n= int(input("enter the number of elements"))
sum=0
for el in range(1,n+1):
    sum+=el
    print(el)
print(sum)


#WAP to find the factorial of first n natural  numbers using while

nums= int(input("enter the number of elements"))

fact=1
indx=1

while indx<=nums:
    fact*=indx
    indx+=1
print(fact)
