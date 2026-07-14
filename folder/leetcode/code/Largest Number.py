class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        # 1. Convert all numbers to strings
        # 2. Sort using a native look-ahead expansion multiplier trick.
        # Since max number length is 10 digits (from 10^9 constraint),
        # repeating a string 10 times standardizes the comparison prefix naturally.
        
        str_nums = sorted([str(num) for num in nums], key=lambda x: x * 10, reverse=True)
        
        # 3. Concatenate the sorted results together
        result = "".join(str_nums)
        
        # 4. Fast check for leading zero edge case
        if result[0] == "0":
            return "0"
            
        return result
