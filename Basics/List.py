#Lists is a built in data type that stores set of values
#It can store elements of different types (integer,float,string,etc)
# Strings are immutable (cant be changed)
# Lists are mutable 

marks=[20,22,24,28]
students=["Joe","Smith","Ryan","Philip"]
student=["Joe",21,"Castroville"]
students[0]="John"

print(students)
print(len(marks))

#List slicing
#Similar to string slicing

#list_name[starting_index:ending_index] #ending index is not included


print(marks[1:3]) # is [22,24]
print(marks[:3]) # is same as [0:3] [20,22,24]
print(marks[1:]) #is same as [1:len(marks)] [22,24,28]
print(marks[-3:-2]) # is [22]

#list methods

list= [2,1,3,4]

list.append(5) #adds one lement at the end
print(list) 

list.sort() #sorts in ascending order
print(list)

list.sort(reverse=True)
print(list)

list.reverse()
print(list)

list.insert(2,8)
print(list)

list.remove(4) # removes first occurance of element
print(list)

list.pop(4) #pops of the element at index
print(list)

#Tuples a built in data type that lets us create immutable sequences of values
#immutable cant change values

tuple = (2,3,4,5,3)
tup=("hello",)
print(type(tuple))
print(type(tup))
print(tuple[3])

#tuple methods

print(tuple.index(2)) #returns index of first occurence
print(tuple.count(3))  #counts total occurances

