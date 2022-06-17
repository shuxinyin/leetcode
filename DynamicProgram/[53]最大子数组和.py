# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。 
# 
#  子数组 是数组中的一个连续部分。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1]
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [5,4,-1,7,8]
# 输出：23
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
# 
#  
# 
#  进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。 
#  Related Topics 数组 分治 动态规划 👍 4998 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        '''reference:https://leetcode.cn/problems/maximum-subarray/solution/dong-tai-gui-hua-fen-zhi-fa-python-dai-ma-java-dai/

        状态: dp[i] 表示以nums[i] 结尾 的 连续 子数组的最大和
        转移： 根据状态的定义，由于nums[i]一定会被选取。
            正常数组 nums 的值全都>=0时，那么有 dp[i] = dp[i - 1] + nums[i]
            现在存在nums[i]为负的情况，那就讨论一下：
                if nums[i]>0: dp[i] = dp[i - 1] + nums[i]。
                if nums[i]<=0: dp[i] = dp[i - 1]。
            综合起来： dp[i]=max{nums[i],dp[i−1]+nums[i]}
        初始状态： dp[0] = nums[0]
        返回： max(dp)  (多提一下， 平常习惯的应该是dp[i]=max{dp[i-1],dp[i−1]+nums[i]}, return dp[-1] 但这里状态定义不一样了)

        '''
        n = len(nums)

        if n == 0:
            return 0
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        return max(dp)

    def maxSubArray2(self, nums: List[int]) -> int:
        # 由于状态转移方程中，dp[i]只和 dp[i - 1] 有关，可以使用滚动变量方式进行优化
        n = len(nums)
        pre = 0
        res = nums[0]
        for i in range(n):
            pre = max(nums[i], pre + nums[i])
            res = max(res, pre)
        return res

# leetcode submit region end(Prohibit modification and deletion)
