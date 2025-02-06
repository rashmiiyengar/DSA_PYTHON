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