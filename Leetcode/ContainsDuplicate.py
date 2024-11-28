from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen=set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        
        return False

solution = Solution()

nums =[1,1,1,2,2,3,4]
value=solution.removeDuplicates(nums)
print(value)
