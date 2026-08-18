from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r, d, n = deque(i for i, c in enumerate(senate) if c == 'R'), deque(i for i, c in enumerate(senate) if c == 'D'), len(senate)
        while r and d: r.append(r.popleft() + n) if r[0] < d[0] else d.append(d.popleft() + n); d.popleft() if r[-1] > d[-1] else r.popleft()
        return "Radiant" if r else "Dire"
