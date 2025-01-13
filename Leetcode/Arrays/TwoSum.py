from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       dict={}
       for i in range(len(nums)):
            diff = target-nums[i]
            if(diff in dict):
                return [dict[diff],i]
            dict[nums[i]]=i

solution = Solution()

nums =[2,7,11,15]
list =solution.twoSum(nums,9)
print(list)