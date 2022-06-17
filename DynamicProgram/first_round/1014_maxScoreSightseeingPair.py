class Solution:
    def maxScoreSightseeingPair(self, nums: List[int]) -> int:
        res = 0
        max_pre = nums[0] + 0

        for i in range(1, len(nums)):
            res = max(res, nums[i] - i + max_pre)
            max_pre = max(max_pre, nums[i] + i)
        return res
