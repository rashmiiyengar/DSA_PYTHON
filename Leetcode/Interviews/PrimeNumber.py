def printPrimeNumbers(nums):
    for num in nums:
        if num <=1:
            continue
        is_prime=True
        
        #Iterate from 2 to n/2
        for i in range(2,int(num**0.5)+1):
            if num %i ==0:
                is_prime=False
                break
        
        if is_prime:
            print(num)
    
nums=[1,2,3,4,5,6,7,8]
printPrimeNumbers(nums)
