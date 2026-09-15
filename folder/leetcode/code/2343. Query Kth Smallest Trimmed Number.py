class Solution:
    def smallestTrimmedNumbers(self, nums: list[str], queries: list[list[int]]) -> list[int]:
        return [sorted([(s[-t:], i) for i, s in enumerate(nums)], key=lambda x: (x[0], x[1]))[k - 1][1] for k, t in queries]
