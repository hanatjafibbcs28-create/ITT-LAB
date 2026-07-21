from functools import cache
class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False  
        n = len(s1)
        for i in range(1, n):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[n-i:]) and self.isScramble(s1[i:], s2[:n-i]):
                return True      
        return False

                                           (or)

  class Solution:
    def __init__(self):
        self.map = {}
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if s1 == s2:
            return True
        state_key = (s1, s2)
        if state_key in self.map:
            return self.map[state_key]
        a, b, c = [0] * 26, [0] * 26, [0] * 26
        for i in range(1, n):
            j = n - i
            a[ord(s1[i - 1]) - 97] += 1
            b[ord(s2[i - 1]) - 97] += 1
            c[ord(s2[j]) - 97] += 1
            if a == b and self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                self.map[state_key] = True
                return True
            if a == c and self.isScramble(s1[:i], s2[j:]) and self.isScramble(s1[i:], s2[:j]):
                self.map[state_key] = True
                return True
        self.map[state_key] = False
        return False
