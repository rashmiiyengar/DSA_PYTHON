str = "This is a string"
str1 ="This is another string"
str2 = "This is escape sequence \n string" #next line
str3 = "This is escape sequence \t string" #Tab 

print(len(str))
print(str.split(' '))
print(str2)

print(str+str1) # Concatination
print(str[-1])


#Slicing
#str[starting_index :ending_index] #ending index is not included
print(str[1:3]) # hi
print(str[0:3]) # Thi
print(str[1:]) # this is same as str[1:len(str)]
print(str[ :4]) # is same as str[0:4]