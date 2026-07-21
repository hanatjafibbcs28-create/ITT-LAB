from collections import Counter
class Solution:
    def sortString(self, s: str) -> str:
        counts = Counter(s)
        unique_chars = sorted(counts.keys())  
        res = []
        n = len(s)
        while len(res) < n:
            for char in unique_chars:
                if counts[char] > 0:
                    res.append(char)
                    counts[char] -= 1
            for char in reversed(unique_chars):
                if counts[char] > 0:
                    res.append(char)
                    counts[char] -= 1  
        return "".join(res)
