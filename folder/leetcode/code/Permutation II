class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        result = []
        current_permutation = []
        
        # 1. Sort the numbers so duplicates are next to each other
        nums.sort()
        
        # 2. Keep track of which numbers we have already used in our current path
        used = [False] * len(nums)
        
        def backtrack():
            # Base case: If our path is as long as nums, we found a valid permutation
            if len(current_permutation) == len(nums):
                result.append(list(current_permutation)) # Use list() to make a copy
                return
            
            for i in range(len(nums)):
                # Skip if we already used this exact element in the current path
                if used[i]:
                    continue
                
                # Crucial Duplicate Skip Condition:
                # If this number is the same as the previous number, AND the previous
                # number hasn't been used yet in this turn, skip it to avoid duplicates.
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                # Make a choice
                used[i] = True
                current_permutation.append(nums[i])
                
                # Recursively build the rest of the permutation
                backtrack()
                
                # Undo the choice (Backtrack)
                current_permutation.pop()
                used[i] = False
                
        # Start the recursive process
        backtrack()
        return result
