from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}
        
        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                return True
            
            index_map[num] = i
        
        return False
    
solution = Solution()

nums = [1,2,3,1]
value=solution.containsNearbyDuplicate(nums,3)
print(value)