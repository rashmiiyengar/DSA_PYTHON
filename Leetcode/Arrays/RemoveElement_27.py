from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        n=len(nums)

        while i<n:
            if nums[i] == val:
                nums[i]=nums[n-1]
                n-=1
            else:
                i+=1
                
        return n
    
solution = Solution()

nums =[1,3,4,2,2,3,9]
value=solution.removeElement(nums,2)
print(value)
