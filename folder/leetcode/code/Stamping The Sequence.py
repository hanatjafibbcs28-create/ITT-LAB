class Solution:
    def movesToStamp(self, stamp: str, target: str) -> list[int]:
        M, N = len(stamp), len(target)
        t_list = list(target)
        res = []
        changed = True
        def can_stamp(i):
            matched = False
            for j in range(M):
                if t_list[i + j] == '?':
                    continue
                if t_list[i + j] != stamp[j]:
                    return False
                matched = True 
            return matched
        while changed:
            changed = False
            for i in range(N - M + 1):
                if can_stamp(i):
                    for j in range(M):
                        t_list[i + j] = '?'
                    res.append(i)
                    changed = True
        return res[::-1] if all(c == '?' for c in t_list) else []
