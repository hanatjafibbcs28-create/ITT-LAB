class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        last = -200
        idx1 = -1
        idx2 = -1

        for i in range(n-1, -1, -1):
            if nums[i] >= last:
                last = nums[i]
                continue
            else:
                idx1 = i
                break
        
        if idx1 == -1:
            nums.reverse()
            return
        
        for i in range(n-1, idx1, -1):
            if nums[i] > nums[idx1]:
                idx2 = i
                break
        
        
        nums[idx1], nums[idx2] = nums[idx2], nums[idx1]

        nums[idx1+1:n] = nums[idx1+1:n][::-1]
