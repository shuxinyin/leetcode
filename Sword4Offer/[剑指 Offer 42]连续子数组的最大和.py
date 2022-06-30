# 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。 
# 
#  要求时间复杂度为O(n)。 
# 
#  
# 
#  示例1: 
# 
#  输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 10^5 
#  -100 <= arr[i] <= 100 
#  
# 
#  注意：本题与主站 53 题相同：https://leetcode-cn.com/problems/maximum-subarray/ 
# 
#  
#  Related Topics 数组 分治 动态规划 👍 545 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''同 53
        状态：dp[i]表示nums[i]结尾的最大子数组和
        转移： if nums[i] > 0: dp[i]=dp[i-1] +  nums[i]
                if nums[i] < 0: dp[i]=dp[i-1]
        综合起来： dp[i]=max{nums[i],dp[i−1]+nums[i]}
        初始状态： dp[0]=nums[0]
        '''
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        return max(dp)
# leetcode submit region end(Prohibit modification and deletion)
