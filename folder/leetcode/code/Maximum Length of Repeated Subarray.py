class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        if len(nums1) < len(nums2): nums1, nums2 = nums2, nums1
        dp = [0] * (len(nums2) + 1)
        ans = 0
        for i in range(len(nums1)):
            for j in range(len(nums2) - 1, -1, -1):
                dp[j + 1] = dp[j] + 1 if nums1[i] == nums2[j] else 0
                if dp[j + 1] > ans: ans = dp[j + 1]
        return ans
