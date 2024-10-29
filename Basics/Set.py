dict={
    "table":["a peice od furniture","list of facts"],
    "cat":"a small animal"
}

print(dict)

#you are given a list of subjects for students. Assume one classroom is required 
# for 1 subject. how many classrooms are needed by all students
#Case sensitive
subjects={"python","Java","c++","javascript","C"}

print("Total number of classrooms needed :" ,len(subjects))


#WAP ro enter markes of 3 subjects from a user and store them in a dictionry
#start with empty dictionry and add one by ine 
# use subject name as key and marks as value
marks={}
print(type(marks))

chemistryMarks=int(input("enter markes for chemistry"))
physicsMarks=int(input("enter markes for physics"))
mathMarks=int(input("enter markes for math"))
marks.update({"chemistry":chemistryMarks})
marks.update({"physics":physicsMarks})
marks.update({"mathMarks":mathMarks})

print(marks)


#Figure out a way to store 9 and 9.0 as separate values in set

collection4 ={9,9.0}

values={
    ("float",9.0),
    ("int",9)
}
print(collection4)
print(values)