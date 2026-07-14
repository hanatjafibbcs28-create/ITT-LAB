from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. Length check shortcut: exit immediately if lengths differ
        if len(s) != len(t):
            return False
            
        # 2. Native C-level frequency map evaluation
        return Counter(s) == Counter(t)
