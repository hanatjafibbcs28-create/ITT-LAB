class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        total_sum = 0
        max_sum = nums[0]
        curr_max = 0
        min_sum = nums[0]
        curr_min = 0
        for num in nums:
            total_sum += num
            curr_max = max(num, curr_max + num)
            max_sum = max(max_sum, curr_max)
            curr_min = min(num, curr_min + num)
            min_sum = min(min_sum, curr_min)
        if max_sum < 0:
            return max_sum
        return max(max_sum, total_sum - min_sum)
