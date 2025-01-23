def swapTwoNumsWithoutThirdVar(a,b):
    a=a+b
    b=a-b
    a=a-b
    
    return a,b

result=swapTwoNumsWithoutThirdVar(22,45)
print(result)
    
    

