import math


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1, count2 = 0, 0
        cand1, cand2 = None, None
        for n in nums:
            if n == cand1:
                count1 += 1
            elif n == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = n
                count1 = 1
            elif count2 == 0:
                cand2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        ans = []
        if nums.count(cand1) > math.floor(len(nums) / 3):
            ans.append(cand1)
        if nums.count(cand2) > math.floor(len(nums) / 3):
            ans.append(cand2)
        return ans
