class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        l, s, z, ans = 0, 0, 0, 0
        for r, n in enumerate(nums):
            s, z = s + n, (0 if n else z)
            while l < r and (s > goal or (s == goal and not nums[l])): s, z, l = s - nums[l], z + (1 if s == goal else 0), l + 1
            if s == goal: ans += 1 + z
        return ans
