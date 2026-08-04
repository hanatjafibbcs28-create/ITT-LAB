class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []
        p_count = [0] * 26
        s_count = [0] * 26
        for i in range(np):
            p_count[ord(p[i]) - ord('a')] += 1
            s_count[ord(s[i]) - ord('a')] += 1
        res = []
        if p_count == s_count:
            res.append(0)
        for i in range(np, ns):
            s_count[ord(s[i]) - ord('a')] += 1
            s_count[ord(s[i - np]) - ord('a')] -= 1
            if s_count == p_count:
                res.append(i - np + 1)
        return res
