class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        n = len(nums)
        memo = {}
        def get_max_score_diff(i: int, j: int) -> int:
            if i == j:
                return nums[i]
            if (i, j) in memo:
                return memo[(i, j)]
            pick_left = nums[i] - get_max_score_diff(i + 1, j)
            pick_right = nums[j] - get_max_score_diff(i, j - 1)
            memo[(i, j)] = max(pick_left, pick_right)
            return memo[(i, j)]
        return get_max_score_diff(0, n - 1) >= 0
