from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        curr_sum=0

        for i in range(k):
            curr_sum+=nums[i]
        
        max_avg= curr_sum / k

        for i in range(k,n):
            curr_sum+=nums[i]
            curr_sum-=nums[i-k]

            avg=curr_sum/k
            max_avg=max(max_avg,avg)
        return max_avg
    
solution = Solution()

nums = [1,2,-5,12,4,3,1]
value=solution.findMaxAverage(nums,4)
print(value)