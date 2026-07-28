class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        i = 2
        for n in nums[2:]:
            if n > nums[i - 2]:
                nums[i] = n
                i += 1
        return i
