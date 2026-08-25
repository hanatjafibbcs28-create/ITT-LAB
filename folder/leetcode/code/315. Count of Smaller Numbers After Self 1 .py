class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
            
        MAX_VAL = 20005
        OFFSET = 10002
        bit = [0] * MAX_VAL
        counts = [0] * len(nums)
        
        def update(index: int, val: int):
            while index < MAX_VAL:
                bit[index] += val
                index += index & (-index)
                
        def query(index: int) -> int:
            total = 0
            while index > 0:
                total += bit[index]
                index -= index & (-index)
            return total

        # Process from right to left
        for i in range(len(nums) - 1, -1, -1):
            shifted_val = nums[i] + OFFSET
            # Query count of elements strictly smaller than the current number
            counts[i] = query(shifted_val - 1)
            # Insert current element into the BIT frequency tracker
            update(shifted_val, 1)
            
        return counts
