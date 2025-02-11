from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l=0

        for r in range(len(nums)):
            if nums[r]:
                nums[l],nums[r] = nums[r], nums[l]
                l+=1
        return nums
    
solution = Solution()

nums = [0,1,5,0,12]
value=solution.moveZeroes(nums)
print(value)