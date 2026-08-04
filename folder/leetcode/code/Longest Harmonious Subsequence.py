from collections import Counter
class Solution:
    def findLHS(self, nums: list[int]) -> int:
        counts = Counter(nums)
        max_length = 0
        for num in counts:
            if num + 1 in counts:
                max_length = max(max_length, counts[num] + counts[num + 1])
        return max_length
