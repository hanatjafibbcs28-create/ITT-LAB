class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1
        
        # 1. Skip all trailing spaces from the end of the string
        while i >= 0 and s[i] == ' ':
            i -= 1
            
        # 2. Count characters until another space or the start of the string is hit
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
            
        return length
