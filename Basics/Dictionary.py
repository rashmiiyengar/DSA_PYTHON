#Dictionaries are used to store data values in key:value pairs
#They are unordered, mutable(changable) & dont allow duplicate keys

dict ={
    "name":"Rashmi",
    "cgpa":9.6,
    "marks":[98,97,99],
    "place":"Texas",
    "isAdult":True,
    "tuple":("ra","sh"),
    12:1
}

str=abc
d={
    
}


dict["name"]=12
print(dict["name"])
print(dict[12])
print(dict["tuple"])
print(dict["tuple"])

student ={
    "name":"Rashmi",
    "cgpa":9.6,
    "score":{
        "chem":99,
        "phy":80
    }
}

print(student)
print(student["score"]["chem"])

#Dictionary methods
print(student.keys()) #Returns all keys in the dictionry
print(student.values()) #Returns all values in the dictionry
print(student.items())  #Returns all (key,val) pairs as tuples
print(student.get("name")) #returns the value of the key , recommended way to get value of key
print(student.update({"citty":"texas"})) #inserts specified items to the dictionry
print(student)

# Set is the collection of unordered items
# each element in the set must be unique and immutable

nums = {1,2,3,4}
set2 ={1,1,2,3,3,0}
# Repeated elements stored only once , so it resolved to {1,2}
#list and dictionries cannot be stored in set as both are mutable

print(type(set2))
print(set2)
print(len(set2))

emptyset=set()
print(type(emptyset))

nums.add(5) # adds an element
print(nums)

nums.remove(5) # removes an element
print(nums)

nums.clear() #empties the set
print(nums)
 
nums.add(5)
nums.add(2)
nums.add(4)
print(nums)



collection = set()
collection.add(1)
collection.add(2)
collection.add("rashmi")
collection.add((2,2,2))
# collection.add([2,2,2]) unhashable type
# immutable -> hashvalue can be created only for immutable values
# so we cant add list or dictionry to set as hashvalue is bound to change in future
print(len(collection))
collection1={"hello","how","Are","You","rashmi"}

print("set collection is ",collection)
collection1.pop() #retiurns the popped value
print("set collection1 is ",collection1)

collection3= collection1.union(collection) 
print("New Union collection3 is ",collection3)
print("collection1 is ",collection1)
print("collection is ",collection)

intersectionCollection= collection1.intersection(collection) 
print(intersectionCollection)