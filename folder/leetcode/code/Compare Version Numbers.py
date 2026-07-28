from itertools import zip_longest
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_revisions = (int(x) for x in version1.split('.'))
        v2_revisions = (int(x) for x in version2.split('.'))
        for r1, r2 in zip_longest(v1_revisions, v2_revisions, fillvalue=0):
            if r1 < r2:
                return -1
            if r1 > r2:
                return 1
        return 0
