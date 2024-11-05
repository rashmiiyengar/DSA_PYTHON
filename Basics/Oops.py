# functions reduces redundancy and improves reusablility
# Object oriented programming
class Student:
    college="KIT" #class attribute
    
    #parameterised constructor
    def __init__(self,fullname,marks) -> None:
        self.name = fullname #obj attribute , obj attribute has precedence over class attribute
        self.marks=marks
        print("hello",self.name)
        pass
    
    def createMethod(self):
        print(self.college)
        
    @staticmethod
    def hello():
        print("th")

s= Student("rash",90)
print(s.name,s.marks)
print(s.college)
s.createMethod()
Student.hello()

 