class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # 1. Initialize our candidate and the vote counter
        candidate = None
        count = 0
        
        # 2. Iterate through all the elements in the array
        for num in nums:
            # If the current counter drops to 0, choose a new candidate
            if count == 0:
                candidate = num
            
            # If the current number matches the candidate, increment the vote
            # Otherwise, decrement the vote (cancel each other out)
            if num == candidate:
                count += 1
            else:
                count -= 1
                
        # The problem guarantees a majority element always exists, 
        # so our remaining candidate is automatically the correct answer.
        return candidate
