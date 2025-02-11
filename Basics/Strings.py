str1 ="This is another string"
str2 = "This is escape sequence \n string" #next line
str3 = "This is escape sequence \t string" #Tab 
str = "madam madam"
s=str.lower()
print(s)
s1=s.replace(" ","")
print(s1)
s2= s[::-1]
print(s2)

t=str.lower().replace(' ','')
print(t[::-1])

print(len(str))
print(str.split(' '))
print(str2)

print(str+str1) # Concatination
print(str[-1])

#Slicing
#str[starting_index :ending_index] 
#ending index is not included
print(str[1:3]) # hi
print(str[0:3]) # Thi
print(str[1:]) # this is same as str[1:len(str)]
print(str[ :4]) # is same as str[0:4]
print(str[-3:-2]) # i

# String functions
strFun= "live love laugh"
print(strFun.capitalize()) #captitalizes 1st char
print(strFun.endswith('gh')) #returns true if string ends with substr
print(strFun.replace("live","love")) #replaces all occurences of old with new
print(strFun.find("laugh")) #returns 1st index of 1st occurence
print(strFun.count("l")) #counts the pccurences of substr in string

#original string is not changed until you explicitly mention
print(strFun)

strFun= strFun.replace("live","love")
print(strFun)

#program to take user input firstname and print length

#firstname=input("Enter user Firstname:")
#print(firstname)
#print("length of firstname is",len(firstname))

#Conditional statements 
#if-elif-else
#indentation important
age=1

if(age>=21):
    print("can vote")
elif(age>13 and age<21):
    print("you are still teen, cant vote")
else:
    print("Not eligble for voting")
    
#nesting
age1 = 8

if(age1>=18):
    if(age>=80):
        print("cannot drive as you neeed assistance")
    print("can drive")
else:
    print("cannot vote")
    
#WAP to check if number entered by user is odd or even
num = 3

if(num%2==0):
    print(num, "is even number")
else:
    print(num,"is odd number")
    
#WAP to find the greatest of 3 numbers entered by the user
a=2
b=3
c=4

if(a>b and a>c):
    print(a, "is greatest num")
elif(b>a and b>c):
    print(b,"is greatest num")
elif(c>a and c>b):
    print(c,"is greates num")
    
#WAP to check if a number is multiple of 7 or not
num1=10

if(num1%7==0):
    print(num1,"is multiple of 7")
else:
    print(num1,"is not multiple of 7")