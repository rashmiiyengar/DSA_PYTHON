# Functions reduces redundancy and improves reusablility
# Object oriented programming
class Student:
    #Class attribute
    college="KIT" 
    
    #Parameterised constructor
    def __init__(self,fullname,marks) -> None:
        #Obj attribute , Obj attribute has precedence over class attribute
        self.name = fullname 
        self.marks=marks
        print("hello",self.name)
        pass
    
    def createMethod(self):
        print(self.college)
        
    @staticmethod
    def hello():
        print("Static method")

s= Student("rash",90)
print(s.name,s.marks)
print(s.college)
s.createMethod()
Student.hello()