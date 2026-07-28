import bisect
class MedianFinder:
    def __init__(self):
        self.buckets = [[] for _ in range(401)]
        self.b_counts = [0] * 401
        self.total = 0
    def addNum(self, num: int) -> None:
        self.total += 1
        b_idx = (num + 100000) // 500
        bisect.insort(self.buckets[b_idx], num)
        self.b_counts[b_idx] += 1
    def findMedian(self) -> float:
        mid_idx = self.total // 2
        count = 0
        for i in range(401):
            if count + self.b_counts[i] > mid_idx:
                local_idx = mid_idx - count
                block = self.buckets[i]
                if self.total % 2 == 1:
                    return float(block[local_idx])
                else:
                    if local_idx == 0:
                        prev_idx = i - 1
                        while self.b_counts[prev_idx] == 0:
                            prev_idx -= 1
                        return (self.buckets[prev_idx][-1] + block[local_idx]) / 2.0
                    return (block[local_idx - 1] + block[local_idx]) / 2.0
            count += self.b_counts[i]
