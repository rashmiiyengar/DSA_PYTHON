#Start: m + n - 1 is the starting value. 
#The loop will begin from this value.
#Stop: -1 is the stopping value. 
#The loop will end before reaching -1.
#Step: -1 is the step value. 
#This means the loop will decrement by 1 on each iteration, moving in reverse order.

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
       
        x= m-1
        y= n-1
    
        for z in range(m + n - 1, -1 ,-1):
            if x < 0:
                nums1[z] = nums2[y]
                y-=1
            elif y < 0:
                break
            elif nums1[x] > nums2[y]:
                nums1[z] = nums1[x]
                x-=1
            else:
                nums1[z] = nums2[y]
                y-=1
        print(nums1)
        
solution = Solution()
solution.merge([1,2,3,0,0,0],3,[2,5,6],3)
#Three pointer approach using z 
#o(n+m)
