import math

class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        n = len(nums)
        
        # 1. Base case: If the array contains less than 2 elements, return 0
        if n < 2:
            return 0
            
        min_val = min(nums)
        max_val = max(nums)
        
        # If all elements are identical, the maximum gap is 0
        if min_val == max_val:
            return 0
            
        # 2. Calculate the minimum possible maximum gap using the Pigeonhole Principle
        # There are (n - 1) gaps between n sorted numbers.
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1
        
        # 3. Create buckets to store the MIN and MAX value seen in each interval
        # We initialize them to None to easily detect empty buckets
        buckets_min = [None] * bucket_count
        buckets_max = [None] * bucket_count
        
        # 4. Populate the buckets with the min and max values
        for num in nums:
            # Determine which bucket index this number belongs to
            idx = (num - min_val) // bucket_size
            
            if buckets_min[idx] is None:
                buckets_min[idx] = num
                buckets_max[idx] = num
            else:
                buckets_min[idx] = min(buckets_min[idx], num)
                buckets_max[idx] = max(buckets_max[idx], num)
                
        # 5. Scan the buckets from left to right to find the maximum gap
        max_gap = 0
        previous_max = min_val  # Start tracking from the absolute minimum value
        
        for i in range(bucket_count):
            # Skip empty buckets
            if buckets_min[i] is None:
                continue
                
            # The gap is the difference between the current bucket's minimum
            # and the previous non-empty bucket's maximum
            max_gap = max(max_gap, buckets_min[i] - previous_max)
            
            # Update previous_max for the next comparison
            previous_max = buckets_max[i]
            
        return max_gap
