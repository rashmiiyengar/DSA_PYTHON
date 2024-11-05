#Abstraction
# hiding the implementation details of a class and only showing the essential features to user

class Car:
    def __init__(self) -> None:
        self.acc= False
        self.brk=False
        self.clutch=False
    
    def start(self):
        self.clutch=True
        self.acc=True
        print("Car started")
        
car= Car()
car.start()