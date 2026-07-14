class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 1. Set up pointers for the ends of valid elements in both arrays
        p1 = m - 1          # Pointer for the last valid number in nums1
        p2 = n - 1          # Pointer for the last number in nums2
        p = m + n - 1       # Pointer for the very last spot in nums1
        
        # 2. Compare elements from the back and place the larger one at index 'p'
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
            
        # 3. If there are any leftover elements in nums2, copy them over.
        # (Leftovers in nums1 are already in their correct places)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
