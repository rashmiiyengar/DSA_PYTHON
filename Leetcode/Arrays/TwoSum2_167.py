from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        left=0
        right=n-1
        
        while left<right:
            sum= numbers[left] + numbers[right]
            if sum == target:
                return [left,right]
            elif sum < target:
                left+=1
            else:
                right-=1
                
solution = Solution()

nums = [2,7,11,15]
value=solution.twoSum(nums,9)
print(value)
        

        
        