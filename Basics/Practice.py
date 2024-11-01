class Solution:
    def validPalindrome(self, s: str) -> bool:        
        i, j = 0, len(s) - 1
        mid = len(s) // 2
        mismatch_count = 0
        left_ind, right_ind, left_char_removed, right_char_removed = -1, -1, '', ''

        while i <= mid and j >= mid:
            if s[i] != s[j]:
                mismatch_count += 1
                left_ind = i
                right_ind = j
            i += 1
            j -= 1
        
        if left_ind == -1 and right_ind == -1:
            # check whether given string is a palindrome
            return s == s[::-1]
        
        #s = s[0:left_ind] + s[right_ind:len(s)]
        for i in range(len(s)):
            if i != left_ind:
                left_char_removed += s[i]

        for i in range(len(s)):
            if i != right_ind:
                right_char_removed += s[i]
        print(left_char_removed, right_char_removed, mismatch_count)
        
        return mismatch_count <= 1 and (left_char_removed == left_char_removed[::-1] 
                                        or right_char_removed == right_char_removed[::-1])          
                
            
                
st = 'eedede'                
s = Solution()            
print(s.validPalindrome(st))