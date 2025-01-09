from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        s_dictionry = Counter(s)
        t_dictionry = Counter(t)

        return s_dictionry == t_dictionry
