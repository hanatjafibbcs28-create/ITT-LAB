class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        if len(arr) == 1: return 1
        need, prev, ans, consec = 0, arr[0], 1, 1
        for x in arr[1:]:
            curr_sign = (x > prev) - (x < prev)
            if curr_sign == 0: need, consec = 0, 1
            elif need == 0 or curr_sign == need: consec, need = consec + 1, -curr_sign
            else: consec, need = 2, -curr_sign
            if consec > ans: ans = consec
            prev = x
        return ans
        
