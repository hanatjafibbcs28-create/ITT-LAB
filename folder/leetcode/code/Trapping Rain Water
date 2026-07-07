class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        
        # Initialize two pointers at the ends of the array
        left, right = 0, len(height) - 1
        
        # Track the maximum heights seen so far from left and right
        left_max, right_max = height[left], height[right]
        water_trapped = 0
        
        while left < right:
            # The smaller boundary determines the water level limit
            if left_max < right_max:
                left += 1
                # Update max or calculate trapped water for the current bar
                left_max = max(left_max, height[left])
                water_trapped += left_max - height[left]
            else:
                right -= 1
                # Update max or calculate trapped water for the current bar
                right_max = max(right_max, height[right])
                water_trapped += right_max - height[right]
                
        return water_trapped
