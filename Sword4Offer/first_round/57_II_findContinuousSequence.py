class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # sliding window
        # Time: O(N),N=len(target)
        # Space: O(1)
        i, j, s, res = 1, 2, 3, []
        while i < j:
            if s == target:
                res.append(list(range(i, j + 1)))
            if s >= target:
                s -= i
                i += 1
            else:
                j += 1
                s += j
        return res

