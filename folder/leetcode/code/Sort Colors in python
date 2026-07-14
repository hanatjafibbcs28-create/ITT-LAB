class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. Initialize three pointers
        low = 0
        current = 0
        high = len(nums) - 1
        
        # 2. Iterate through the array until current meets high
        while current <= high:
            if nums[current] == 0:
                # Found a 0: swap it with the element at low
                nums[current], nums[low] = nums[low], nums[current]
                low += 1
                current += 1
                
            elif nums[current] == 1:
                # Found a 1: it's already in the correct relative zone
                current += 1
                
            else:  # nums[current] == 2
                # Found a 2: swap it with the element at high
                nums[current], nums[high] = nums[high], nums[current]
                high -= 1
                # Do NOT increment current here because the swapped element 
                # from high needs to be evaluated next!
       
