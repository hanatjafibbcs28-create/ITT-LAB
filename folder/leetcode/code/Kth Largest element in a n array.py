class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # 1. Define boundaries based on the constraint: -10^4 <= nums[i] <= 10^4
        MIN_VAL = -10000
        MAX_VAL = 10000
        
        # 2. Create a frequency array to count occurrences of each number
        # Size is (20000 + 1) to safely accommodate the entire range
        range_size = MAX_VAL - MIN_VAL + 1
        count_array = [0] * range_size
        
        # 3. Count frequencies of each number in the input
        # We shift the index by subtracting MIN_VAL so negative numbers map to positive indices
        for num in nums:
            count_array[num - MIN_VAL] += 1
            
        # 4. Walk backwards from the highest possible number to find the kth largest
        remaining_k = k
        for i in range(range_size - 1, -1, -1):
            if count_array[i] > 0:
                remaining_k -= count_array[i]
                
                # If remaining_k <= 0, the current number is the kth largest element
                if remaining_k <= 0:
                    return i + MIN_VAL
                    
        return -1
