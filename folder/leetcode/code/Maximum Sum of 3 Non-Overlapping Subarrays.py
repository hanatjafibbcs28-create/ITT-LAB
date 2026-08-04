class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        w1 = sum(nums[:k])
        w2 = sum(nums[k:2*k])
        w3 = sum(nums[2*k:3*k])
        mx1, mx12, mx123 = w1, w1 + w2, w1 + w2 + w3
        b1, b12, ans = 0, (0, k), [0, k, 2*k]
        for i in range(1, len(nums) - 3*k + 1):
            w1 += nums[i + k - 1] - nums[i - 1]
            w2 += nums[i + 2*k - 1] - nums[i + k - 1]
            w3 += nums[i + 3*k - 1] - nums[i + 2*k - 1]
            if w1 > mx1:
                mx1 = w1
                b1 = i
            if mx1 + w2 > mx12:
                mx12 = mx1 + w2
                b12 = (b1, i + k)
            if mx12 + w3 > mx123:
                mx123 = mx12 + w3
                ans = [b12[0], b12[1], i + 2*k]
        return ans
