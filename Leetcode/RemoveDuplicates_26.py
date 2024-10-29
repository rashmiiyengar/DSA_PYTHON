from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i= 0
        dic={}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]]+=1
            else:
                dic[nums[i]]=1
        j=0
        for i in dic.keys():
            nums[j] = i
            j+=1 
        
        return len(dic)

solution = Solution()

nums =[1,1,1,2,2,3,4]
value=solution.removeDuplicates(nums)
print(value)

        

        