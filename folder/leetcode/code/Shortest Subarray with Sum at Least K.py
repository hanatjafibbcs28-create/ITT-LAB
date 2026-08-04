class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        from collections import deque
        n = len(nums)
        p = [0] * (n + 1)
        for i in range(n): p[i + 1] = p[i] + nums[i]
        q = deque()
        ans = n + 1
        for i in range(n + 1):
            while q and p[i] - p[q[0]] >= k:
                ans = min(ans, i - q.popleft())
            while q and p[i] <= p[q[-1]]:
                q.pop()
            q.append(i)
        return ans if ans <= n else -1
