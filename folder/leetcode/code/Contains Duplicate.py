class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # 1. Early-exit optimization for small lists
        if len(nums) < 2:
            return False
            
        # 2. Sub-sampling trick for massive inputs with early duplicates
        # Checking the first 100 elements directly captures quick duplicates 
        # without running a heavy full-list allocation.
        if len(nums) > 100 and len(nums[:100]) != len(set(nums[:100])):
            return True
            
        # 3. Blazing-fast full set evaluation
        # This executes entirely at the native compiled C level of Python.
        return len(nums) != len(set(nums))
