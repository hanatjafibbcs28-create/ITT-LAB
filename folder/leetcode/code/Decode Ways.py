class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0': return 0
        p2, p1, prev = 1, 1, int(s[0])
        for c in (int(x) for x in s[1:]):
            p2, p1, prev = p1, (p1 if c else 0) + (p2 if 10 <= prev * 10 + c <= 26 else 0), c
            if not p1: return 0
        return p1
