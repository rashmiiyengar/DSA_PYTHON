arr=[3,2,6,8,1,3]

word=['three','two','six','eight','one','three']

person = {'name': 'John', 'age': 30, 'city': 'New York'}

#list comprehension
#[expression for item in iterable if condition]

for key,value in person.items():
    print(f"{key}:{value}")

for num,char in zip(arr,word):
    print(f"{num}:{char}")
# for i in arr:
#     print(i)

# for i in range(0,len(arr)):
#     print(arr[i])
    
for i in range(1,5,2):
    print(i)
    
count=0
while count<6:
    print(count)
    count+=1
    
for index,value in enumerate(arr):
    print(f"{index}:{value}")
    
sq=[x*x for x in range(10) if x%2==0]
print(sq)