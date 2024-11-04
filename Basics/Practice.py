from typing import List

class Solution:
    def longestCommanPrefix(self,strs:List[str])->str:
        min_length= float('inf')
        
        for s in strs:
            if len(s) < min_length:
                min_length = len(s)
    
        i=0
        while i < min_length:
            for s in strs:
                if s[i]!= strs[0][i]:
                    return s[:i]
            i+=1
        
        return s[:i]
            
                    
solution = Solution()
commanPrefix=solution.longestCommanPrefix(["flower","flow","flight"])
print(commanPrefix)