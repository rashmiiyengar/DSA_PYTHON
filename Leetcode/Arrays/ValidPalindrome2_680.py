class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindromeCheck(left,right):
            while left<=right:
                if s[left]!=s[right]:
                    return False
                else:
                    left+=1
                    right-=1
            return True

        left=0
        right=len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return palindromeCheck(left+1,right) or palindromeCheck(left,right-1)
            else:
                left+=1
                right-=1

        return True
    
solution = Solution()
result=solution.validPalindrome("abca")
print("The given string is palindrome " ,result)