class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        return sorted(list(set(range(min(nums), max(nums) + 1)) - set(nums)))
