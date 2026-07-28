from string import ascii_lowercase
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        counts = list(map(s.count, ascii_lowercase))
        half = "".join(c * (k // 2) for c, k in zip(ascii_lowercase, counts) if k > 0)
        mid = "".join(c for c, k in zip(ascii_lowercase, counts) if k % 2 == 1)
        return half + mid + half[::-1]
