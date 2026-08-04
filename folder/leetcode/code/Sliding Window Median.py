import heapq
class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        small, large, lazy = [], [], {}
        s_sz, l_sz = 0, 0
        def prune():
            while small and lazy.get(-small[0], 0) > 0: lazy[-heapq.heappop(small)] -= 1
            while large and lazy.get(large[0], 0) > 0: lazy[heapq.heappop(large)] -= 1
        res = []
        for i in range(len(nums)):
            in_val = nums[i]
            if not small or in_val <= -small[0]: heapq.heappush(small, -in_val); s_sz += 1
            else: heapq.heappush(large, in_val); l_sz += 1
            if s_sz > l_sz + 1: heapq.heappush(large, -heapq.heappop(small)); s_sz -= 1; l_sz += 1
            elif l_sz > s_sz: heapq.heappush(small, -heapq.heappop(large)); l_sz -= 1; s_sz += 1
            prune()
            if i >= k - 1:
                res.append(float(-small[0]) if k % 2 == 1 else (-small[0] + large[0]) / 2.0)
                out_val = nums[i - k + 1]
                lazy[out_val] = lazy.get(out_val, 0) + 1
                if out_val <= -small[0]: s_sz -= 1
                else: l_sz -= 1
                if s_sz > l_sz + 1: heapq.heappush(large, -heapq.heappop(small)); s_sz -= 1; l_sz += 1
                elif l_sz > s_sz: heapq.heappush(small, -heapq.heappop(large)); l_sz -= 1; s_sz += 1
                prune()
        return res
