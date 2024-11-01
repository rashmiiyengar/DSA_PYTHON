def func_name():
    print("hello2")
    return True
    
func_name()

#build in functions
print()
len("77")
type("ta")
range(1,2)


#WAP to print the length of a list (list is the parameter)

list=[1,2,3,4,5,6,7,8]

def printAllListEle(list):
    for item in list:
        print(item," ")
        
printAllListEle(list)
    
#WAP to find factorial of n (n is parameter)

def printFactorial(n):
    factorial=1
    index=1
    while index<=n:
        factorial*=index
        index+=1
    print(factorial)
    
printFactorial(7)

#WAP to convert USD to INR

def convertDollarsToInr(dollar):
    
    pricePerDollar=82.14
    dollarToIndianRuppe = dollar * pricePerDollar
    print(f"${dollar} is {int(dollarToIndianRuppe)} Indian Rupee")
    
convertDollarsToInr(3)