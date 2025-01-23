def fibbonacci(n):
    a,b=0,1
    
    for _ in range(n):
        print(a, end=" ")
        a,b=b,a+b
    
num= 6
fibbonacci(num)