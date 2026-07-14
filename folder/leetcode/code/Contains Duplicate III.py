class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        # 1. Base check: if constraints are impossible, return False
        if valueDiff < 0:
            return False
            
        # This hash map acts as our dynamic sliding window of buckets
        buckets = {}
        
        # 2. Width of each bucket must group values within valueDiff range
        # Adding 1 handles cases where valueDiff = 0 to prevent division by zero
        w = valueDiff + 1
        
        for i in range(len(nums)):
            # 3. Identify which bucket the current number belongs to
            # Floor division maps nearby numbers into the same integer index slot
            bucket_id = nums[i] // w
            
            # Condition A: If the exact same bucket already has an element, 
            # the absolute difference between them is guaranteed to be <= valueDiff
            if bucket_id in buckets:
                return True
                
            # Condition B: Check the neighboring bucket to the left
            if (bucket_id - 1) in buckets and abs(nums[i] - buckets[bucket_id - 1]) <= valueDiff:
                return True
                
            # Condition C: Check the neighboring bucket to the right
            if (bucket_id + 1) in buckets and abs(nums[i] - buckets[bucket_id + 1]) <= valueDiff:
                return True
                
            # 4. Save the current number into its computed bucket slot
            buckets[bucket_id] = nums[i]
            
            # 5. Maintain the sliding window size restriction (abs(i - j) <= indexDiff)
            # Remove the oldest element outside the window boundary from our map
            if i >= indexDiff:
                old_bucket_id = nums[i - indexDiff] // w
                del buckets[old_bucket_id]
                
        return False
