class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars = filter(str.isalnum, s)
        cleaned = "".join(filtered_chars).lower()
        return cleaned == cleaned[::-1]
