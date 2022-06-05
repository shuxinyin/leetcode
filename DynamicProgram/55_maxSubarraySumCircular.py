class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total, n = 0, len(nums)
        maxSum, curMax = nums[0], 0
        minSum, curMin = nums[0], 0

        for i in range(n):
            # 最大的连续子集和
            curMax = max(nums[i], curMax + nums[i])
            maxSum = max(maxSum, curMax)

            # 最小的连续子集和
            curMin = min(nums[i], curMin + nums[i])
            minSum = min(minSum, curMin)

            total += nums[i]
        return max(maxSum, total-minSum) if maxSum > 0 else maxSum
