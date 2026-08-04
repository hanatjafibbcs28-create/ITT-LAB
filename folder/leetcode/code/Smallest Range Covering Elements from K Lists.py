class Solution:
    def smallestRange(self, nums: list[list[list[int]]]) -> list[int]:
        flat = sorted((val, i) for i, row in enumerate(nums) for val in row)
        k = len(nums)
        counts = {}
        distinct = 0
        left = 0
        ans = [float('-inf'), float('inf')]
        for right in range(len(flat)):
            r_val, r_list = flat[right]
            counts[r_list] = counts.get(r_list, 0) + 1
            if counts[r_list] == 1: distinct += 1
            while distinct == k:
                l_val, l_list = flat[left]
                if r_val - l_val < ans[1] - ans[0]: ans = [l_val, r_val]
                counts[l_list] -= 1
                if counts[l_list] == 0: distinct -= 1
                left += 1
        return ans
