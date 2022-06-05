class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        # Time: O(log(N)), Space: O(1)
        状态定义：列表dp， dp[i]表示以nums[i]为结尾的子数组的最大连续子数组最大和
        转移方程：若dp[i-1]<=0, 说明dp[i-1]对dp[i]产生负贡献，即dp[i-1]+nums[i]不如nums[i]本身大
                1. dp[i-1] > 0: dp[i] = dp[i-1] + nums[i]
                2. dp[i-1] <= 0: dp[i] = nums[i]
        初始状态： dp[0]=nums[0], 以nums[0]为结尾的子数组的最大连续子数组最大和nums[0]
        返回值： 返回dp中的最大值，代表全局最大值
        '''
        pre, max_dp = 0, nums[0]
        for i in range(0, len(nums)):
            pre = max(pre + nums[i], nums[i])
            max_dp = max(max_dp, pre)

        return max_dp
