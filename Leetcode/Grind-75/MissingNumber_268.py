from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n= len(nums)
        sum_all = n* (n+1)//2
        return sum_all - sum(nums)        
    
solution = Solution()

nums =[0,3,1]
list =solution.missingNumber(nums)
print(list)

# nums=[1,2,3,4,6]
# n=len(nums)+1
# sum_all=n*(n+1)//2
# print(sum_all)
# print(sum_all-sum(nums))
# for numbers starting from 0 to n-1 in array take n=len(nums)
# for numbers startinmg from 1 to n-1 in array take n =len(nums)+1