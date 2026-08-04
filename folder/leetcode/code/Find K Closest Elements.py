class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        low, high = 0, len(arr) - k
        while low < high:
            mid = (low + high) // 2
            if x - arr[mid] > arr[mid + k] - x: low = mid + 1
            else: high = mid
        return arr[low : low + k]
