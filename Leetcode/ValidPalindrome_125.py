class Solution:
    def isPalindrome(self, s: str) -> bool:
        if(s==' '):
            return True
        
        s = s.lower()

        updatedStr = ""
        for char in s:
            if char.isalnum():
                updatedStr += char
        
        return True if updatedStr == updatedStr[::-1] else False 
    
solution = Solution()
result=solution.isPalindrome("A man, a plan, a canal: Panama")
print("The given string is palindrome " ,result)