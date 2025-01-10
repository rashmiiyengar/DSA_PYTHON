from typing import List

#Given an array of integers nums which is sorted 
#in ascending order, and an integer target, 
#Write a function to search target in nums.
#If target exists, then return its index. Otherwise, return -1.

#You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left =0
        right = len(nums)-1

        while left<=right:
            middle = (left+right)//2
            if nums[middle]==target:
                return middle
            elif nums[middle]>target:
                right= middle-1
            elif nums[middle]<target:
                left= middle+1

        return -1
        
