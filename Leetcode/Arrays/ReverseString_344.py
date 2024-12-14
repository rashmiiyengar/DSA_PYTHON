from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)
        l=0
        r=n-1
        s[::-1]
        while l<r:
            s[l],s[r] = s[r],s[l]
            l+=1
            r-=1
            
solution = Solution()

s=["h","e","l","l","o"]
solution.reverseString(s)
print(s)