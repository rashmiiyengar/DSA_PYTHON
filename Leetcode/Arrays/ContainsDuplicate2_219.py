#Brute Force
# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i] == nums[j] and abs(i-j)<=k:
#                     return True
#         return False

from ast import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict={}
        
        for i,num in enumerate(nums):
            if num in dict and i-dict[num]<=k:
                return True
            
            dict[num]=i
        return False
solution = Solution()

nums = [1,2,3,1]
value=solution.containsNearbyDuplicate(nums,3)
print(value)