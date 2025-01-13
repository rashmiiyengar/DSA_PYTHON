def shift_even_odd_numbers(nums):
    left,right=0,len(nums)-1
    
    while left<right:
        if nums[left]%2==0:
            left+=1
        elif nums[right]%2!=0:
            right-=1
        else:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
        
    return nums

nums=[1,2,3,4,5,7]

result=shift_even_odd_numbers(nums)
print(result)