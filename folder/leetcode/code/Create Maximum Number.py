class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        m, n = len(nums1), len(nums2)
        def maxSubarray(nums, size):
            stack = []
            drop = len(nums) - size
            for num in nums:
                while drop > 0 and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:size]   
        def merge(sub1, sub2):
            # Using an iterator approach allows Python's native max() 
            # to choose the larger list instantly at C-speed
            return [max(sub1, sub2).pop(0) for _ in range(len(sub1) + len(sub2))]
        best = []
        for i in range(max(0, k - n), min(k, m) + 1):
            sub1 = maxSubarray(nums1, i)
            sub2 = maxSubarray(nums2, k - i)
            candidate = merge(sub1, sub2)
            if candidate > best:
                best = candidate   
        return best
