from typing import List


class Solution:
    def majorityElement(self,nums:List[int])->int:
        dic={}
        n=len(nums)/2
        i=0
        
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]]+=1
            else:
                dic[nums[i]]=1
        
        for key,value in dic.items():
            if value > len(nums)/2:
                return key
        
        
solution=Solution()
result=solution.majorityElement([3,2,3])
print(result)