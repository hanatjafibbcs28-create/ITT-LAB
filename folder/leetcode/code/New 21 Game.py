class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts: return 1.0
        dp = [1.0] + [0.0] * maxPts
        window_sum, ans = 1.0, 0.0
        for i in range(1, n + 1):
            curr = window_sum / maxPts
            if i >= k: ans += curr
            if i < k: window_sum += curr
            if i >= maxPts: window_sum -= dp[(i - maxPts) % (maxPts + 1)]
            dp[i % (maxPts + 1)] = curr
        return ans
