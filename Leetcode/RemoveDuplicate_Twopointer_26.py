from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n= len(nums)
        j=1

        for i in range(1,n):
           if nums[i] != nums[i-1]:
                nums[j]= nums[i]
                j+=1
        
        return j
        # Time:O(n)
        # Space: o(1)

solution = Solution()

nums =[1,1,1,2,2,3,4]
value=solution.removeDuplicates(nums)
print(value)